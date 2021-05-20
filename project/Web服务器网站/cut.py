import jieba
import wordcloud as WC
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
mask=np.array(Image.open("five.png"))
words=WC.WordCloud(font_path="simkai.ttf",mask=mask,
                   background_color="white",
                   max_words=200,width=80,height=100,random_state=42,max_font_size=50)
with open("douban_comments.txt","r+",encoding="GBK") as fp:
    text=fp.read()
text=" ".join(jieba.lcut(text))
words.generate(text)
plt.imshow(words)
plt.axis("off")
plt.show()