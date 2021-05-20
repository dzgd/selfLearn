
''''################客户端GET方式发送数据#############
import urllib.request
url=" http://127.0.0.1:5000/"
try:
    p="四川"
    c="广安"
    p=urllib.parse.quote(p)
    c=urllib.parse.quote(c)
    data="province="+p+"&city="+c
    resp=urllib.request.urlopen(url+"?"+data)
    data=resp.read()
    html=data.decode()
    print(html)
except Exception as err:
    print(err)'''





################客户端POST方式发送数据#############
import urllib.request
url=" http://127.0.0.1:5000/"
try:
    p="四川"
    c="广安"
    note="我不止一次地想，如果有上辈子，我们一定遇见过。或许是在那庭院深深中，我是不懂事的孩童，你是长须飘飘、知识渊博的老者，躺在吱呀吱呀的木椅上给我讲述动人的故事；或许是在古老的小巷，下过雨后的梧桐散发出阵阵清香，我伫立青石板上翘首等待，你踏马飞奔而来，教会我思考与感悟；或许是在水势湍急的忘川河边，我喝下孟婆汤，走过奈何桥，而你在另一头目送我的远去，我忘记了你的面容，\
    却记得你说过的关于哲理和人性。在翻开你的时候，那沉重的大钟声已悄然停止，那轻快的表秒已凝固留滞，我的呼吸也变得轻浅起来，仿佛一小片洁白无瑕的羽翼落入心头，轻轻痒痒，欲罢不能。\
细细聆听，微风正在轻轻吟唱，过客匆匆留下细碎的脚步声，远方阁楼顶上的那只黑色的老猫，眼睛发出幽绿的光芒，慵懒地呵欠一声便逃窜。遇见你，是上苍赐予我最好的礼物，在温柔岁月里，在安稳现实中，只一眼，我便将你妥帖安放在心"
    p=urllib.parse.quote(p)
    c=urllib.parse.quote(c)
    note=urllib.parse.quote(note)
    data="province="+p+"&city="+c+"&note="+note
    data=data.encode()
    resp=urllib.request.urlopen(url,data=data)
    data=resp.read()
    html=data.decode()
    print(html)
except Exception as err:
    print(err)
