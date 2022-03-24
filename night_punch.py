from time import time, strftime, localtime, sleep
import requests
import json
import schedule


class NightPunch(object):
    """
    健康打卡类。
    argvs: {
        name_list: 打卡人员名字
    }
    """
    def __init__(self, name_list):
        self.name_list = name_list
        self.LOG_FILE = "./log/daily.log"
        self.PAYL_DIR = "./payload/"

    def log_write(self, file_path, content):
        """
        以追加形式写日志。
        argvs: {
            file_path: 文件路径,
            content: 写入的内容
        }
        """
        with open(file_path, mode="a+") as f:
            f.write(content)

    def format_time(self):
        """
        返回格式化的当前时间。
        return: {
            str: 年/月/日 时:分:秒.微妙
        }
        """
        cur_time = time()
        return strftime(f"%Y/%m/%d %H:%M:%S.{int((cur_time - int(cur_time))*1000000)}", localtime(cur_time))

    def night_punch(self):
        """
        晚打卡。
        """
        url = f'https://jinshuju.net/graphql/f/kDiOo6'

        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "origin": "https://jinshuju.net",
            "referer": "https://jinshuju.net/f/kDiOo6",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/93.0.4577.82 Safari/537.36 "
        }
        for name in self.name_list:
            with open(f'{self.PAYL_DIR}night_{name}.json') as f:
                payload = json.load(f)
            ret = requests.post(url=url, json=payload, headers=headers)

            if ret.status_code == 200:
                error_info = json.loads(
                    ret.text)['data']['createPublishedFormEntry']['errors']
                if error_info:
                    self.log_write(
                        self.LOG_FILE, f'{self.format_time()}, user={name}, code={ret.status_code}, error={error_info}!\n')
                else:
                    self.log_write(self.LOG_FILE, f'{self.format_time()}, user={name}, code={ret.status_code}, succeed!\n')
            else:
                self.log_write(self.LOG_FILE, f'{self.format_time()}, user={name}, code={ret.status_code}, error={error_info}!\n')


if __name__ == "__main__":
    # 初始化
    name_list = ['xx']
    health_punch_manager = NightPunch(name_list)

    # 循环执行
    schedule.every().day.at("19:09").do(health_punch_manager.night_punch)
    while True:
        schedule.run_pending()
        sleep(300)
