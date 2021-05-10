import os 
import argparse 
import requests
import re 
import sys 
import json 

# python3 run_spark_benchmark_json.py --spark_properties spark_config_info.txt --benchmark_json spark_configs.json

'''
# Order of Precedence

 1. master_url
 2. jars 
 3. configs not related to file (Spark Properties and stuff like --driver-memory, etc.)
 4. file 
 5. configs related to file (e.x. num_years for mortgage, --input/--output/--benchmark for TPC-DS)
'''

def generate_command_list(spark_config_map, benchmark_file, benchmark_file_args):
    spark_gpu_cmd_list = []
    
    # Add Spark Submit Command 
    spark_gpu_cmd_list.append(os.environ["SPARK_HOME"] + "/bin/spark-submit")

    for option in spark_config_map.keys():
        configs_per_option = spark_config_map[option]
        for config in configs_per_option:
            spark_gpu_cmd_list.append(option)
            spark_gpu_cmd_list.append(config)

    spark_gpu_cmd_list.append(benchmark_file)

    # Add python/jarfile configs to spark command list 

    for i in range(len(benchmark_file_args)):
        config_pair = benchmark_file_args[i]
        config_name = list(config_pair.keys())[0]
        config_value = config_pair[config_name]
        spark_gpu_cmd_list.append(config_name)
        spark_gpu_cmd_list.append(config_value)

    return spark_gpu_cmd_list

# Read in Spark Configs from file --> add them to spark_configs map
def update_spark_config_map(spark_configs_file, spark_config_map):

    config_list = open(spark_configs_file,'r').readlines()

    for config in config_list:
        config_info = config.split(' ')
        option, value = config_info[0], config_info[1]

        if option in spark_config_map:
            cur_value = spark_config_map[option]
            cur_value.append(value)
            spark_config_map[option] = cur_value 
        else:
            spark_config_map[option] = [value]

    return spark_config_map

def main():

    parser = argparse.ArgumentParser(description="Generalized Benchmarking Args")
    parser.add_argument("--spark_properties", default="", type=str, help="Path to file with Spark config properties.", required=True) # txt file for now
    parser.add_argument("--benchmark_json", default="", type=str, help='Path to JSON benchmark configuration file.', required=True)
    benchmark_args = parser.parse_args()

    if benchmark_args.benchmark_json == "":
        print("Make sure to specify your benchmark information in a JSON file")
        sys.exit()

    spark_properties_file = benchmark_args.spark_properties
    benchmark_json_filepath = benchmark_args.benchmark_json

    # Load JSON File 
    benchmark_config_file = open(benchmark_json_filepath,)
    benchmark_configs = json.load(benchmark_config_file)

    '''
    todo: Set environment variables pointing to Spark and the cuDF/RAPIDS jars. 

    environment_vars = benchmark_configs["env_vars"]
    for envar in environment_vars:
        envar_name = list(envar.keys())[0]
        envar_value = environment_vars[envar_name]
        os.environ[envar_name] = envar_value 
    '''

    # Spark Config Map 
    spark_config_map = {}

    # Add master_url to Spark config map 
    spark_config_map["--master"] = [benchmark_configs["master_url"]]

    # Add jars to Spark config map
    spark_jars = benchmark_configs["jars"]
    spark_jars_to_str = jars_list_to_str = ','.join(spark_jars)
    spark_config_map["--jars"] = [spark_jars_to_str]

    # Add other configs (e.x. --driver-memory) to Spark config map 
    other_config_info = benchmark_configs["other_configs"]

    for i in range(len(other_config_info)):
        config_pair = other_config_info[i]
        config_name = list(config_pair.keys())[0]
        config_value = config_pair[config_name]
        spark_config_map[config_name] = [config_value]
    
    # Add Spark properties to Spark config Map 
    spark_config_map = update_spark_config_map(spark_properties_file, spark_config_map)

    spark_cmd_list = generate_command_list(spark_config_map, benchmark_configs["benchmark_file"], benchmark_configs["benchmark_file_args"])
    final_spark_command = ' '.join(spark_cmd_list)

    os.system(final_spark_command)

if __name__ == '__main__':
    main()