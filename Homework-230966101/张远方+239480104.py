# 张远方+239480104

import requests

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "文件未找到，请检查文件路径是否正确。"
    except Exception as e:
        return f"发生错误: {e}"

file_path = '文件路径'
text = read_text_from_file(file_path)
print(text)


def make_api_call(url, params=None, headers=None, timeout=10):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        
        response.raise_for_status()
      
        return response.json()
    
    except requests.exceptions.Timeout:
        
        return "错误：请求超时"
    
    except requests.exceptions.ConnectionError:
        
        return "错误，连接出现问题"
    
    except requests.exceptions.HTTPError as err:
        
        return f"HTTP发生错误: {err}"
    
    except requests.exceptions.RequestException as err:
        
        return f"发生错误: {err}"
import jieba
from collections import Counter



def summarize_texts_jieba(texts, top_n=5):
    combined_text = ' '.join(texts)
    sentences = combined_text.split('。')  

    words = jieba.lcut(combined_text)
    filtered_words = [word for word in words if word.strip()]

    word_freq = Counter(filtered_words)

    sentence_scores = {}
    for sentence in sentences:
        for word in jieba.lcut(sentence):
            if word in word_freq:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = 0
                sentence_scores[sentence] += word_freq[word]

    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:top_n]
    return '。'.join(summarized_sentences)

texts = [
    "人工智能是计算机科学的一个分支。",
    "人工智能系统用于执行通常需要人类智能的任务。",
    "一些人工智能应用的例子包括语音识别和图像处理。",
    "人工智能正在改变许多行业，包括医疗和金融。"
]

summary = summarize_texts_jieba(texts, top_n=3)
print(summary)





