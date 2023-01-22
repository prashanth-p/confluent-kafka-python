from confluent_kafka.admin import (AdminClient, NewTopic,
                                   ConfigResource)

from config import config


# return true if topic exists and false if not
def topic_exists(admin, topic):
    metadata = admin.list_topics()
    for t in iter(metadata.topics.values()):
        if t.topic == topic:
            return True
    return False


# create a new topic and returns results dictionary
def create_topic(admin,topic):
    new_topic = NewTopic(topic,num_partitions=6,replication_factor=3)
    result_dict = admin.create_topics([new_topic])
    for topic, future in result_dict.items():
        try:
            future.result()
            print("Topic {} created".format(topic))
        except Exception as e:
            print("failed to create topic {} : {}".format(topic,e))
            

# get max.message.bytes property
def get_max_size(admin,topic):
    resource = ConfigResource('topic',topic)
    result_dict = admin.describe_configs([resource])
    print(result_dict)
    config_entries = result_dict[resource].result()
    max_size = config_entries['max.message.bytes']
    return max_size.value


# set max.message.bytes property
def set_max_size(admin, topic, max_k):
    config_dict = {'max.message.bytes':str(max_k*1024)}
    print(config_dict)
    resource = ConfigResource('topic',topic,config_dict)
    result_dict = admin.alter_configs([resource])
    result_dict[resource].result()
    
if __name__ == '__main__':
    
    # creating the admin client
    admin = AdminClient(config)
    topic_name = 'new_topic_from_python'
    max_msg_k = 50
    
    # create topic if it does not exist:
    if not topic_exists(admin,topic_name):
        create_topic(admin, topic_name)
    
    # check max.message.bytes config and set if needed
    current_max = get_max_size(admin,topic_name)
    print(f'The current max.message.bytes size is: {current_max}')
    print('The required size of max.message.byts size is: ' + str(max_msg_k*1024))
    if current_max != str(max_msg_k * 1024):
        print(f'Topic, {topic_name} max.message.bytes is {current_max}.')
        print('setting new value...')
        set_max_size(admin, topic_name, max_msg_k)

    # Verify config was set 
    new_max = get_max_size(admin, topic_name)
    print(f'Now max.message.bytes for topic {topic_name} is {new_max}')