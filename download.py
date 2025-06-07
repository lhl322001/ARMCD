import wget

# 提取文件ID
file_id = '1Kuuj5VUX-2rJMiYmAp8aNh_ZUGez9WM3'
# 构造确认URL
confirm_url = f'https://drive.google.com/uc?export=download&id={file_id}'

# 下载文件
output = 'downloaded_file'  # 你可以更改为你想要保存的文件名
wget.download(confirm_url, out=output)
