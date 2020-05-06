import os
import sys
from collections import defaultdict


def get_cmd_arg(name):
    d = defaultdict(list)
    for cmd_args in sys.argv[1:]:
        cmd_arg = cmd_args.split('=')
        if len(cmd_arg) == 2:
            d[cmd_arg[0].lstrip('-')].append(cmd_arg[1])

    if name in d:
        return d[name][0]
    else:
        print('Unknown command line arg requested: {}'.format(name))


def get_env_var(name):
    if name in os.environ:
        return os.environ[name]
    else:
        print('Unknown environment variable requested: {}'.format(name))


def get_stream_app_label():
    return get_cmd_arg('spring.cloud.dataflow.stream.app.label')


def get_stream_name():
    return get_cmd_arg('spring.cloud.dataflow.stream.name')


def get_input_channel():
    return get_cmd_arg("spring.cloud.stream.bindings.input.destination")


def get_output_channel():
    return get_cmd_arg("spring.cloud.stream.bindings.output.destination")


def get_kafka_brokers():
    return get_env_var('SPRING_CLOUD_STREAM_KAFKA_BINDER_BROKERS')


def get_kafka_zk_nodes():
    return get_env_var('SPRING_CLOUD_STREAM_KAFKA_BINDER_ZK_NODES')


def get_application_guid():
    return get_env_var('SPRING_CLOUD_APPLICATION_GUID')


def get_application_group():
    return get_env_var('SPRING_CLOUD_APPLICATION_GROUP')
