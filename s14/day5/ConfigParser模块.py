import configparser

# 生成文档
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('ConfigParser.ini', 'w') as configfile:
    config.write(configfile)


# # 读取
# import configparser
# config = configparser.ConfigParser()
# print(config.sections())
#
# print(config.read('ConfigParser.ini'))
#
# print(config.sections())
#
# print('bitbucket.org' in config)
#
# print(config['bitbucket.org']['User'])
#
# topsecret = config['topsecret.server.com']
# print(topsecret['ForwardX11'])
#
# for key in config['bitbucket.org']:
#     print(key)
