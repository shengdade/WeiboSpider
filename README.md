### ����
- ��ȡ����΢����Ϣ����Ϊ΢���ƶ��˵���Ϣ��PC�˸�������ȡ�����Ա��ű�������΢���ƶ�����ȡ��Ϣ

### ����
- �û�id����������΢���ǳ�Ϊ��Dear-�����Ȱ͡���idΪ��1669879400��

### ���
- �û������û��ǳƣ���"Dear-�����Ȱ�"
- ΢�������û���ȫ��΢������ת��΢��+ԭ��΢����
- ��ע�����û���ע��΢���˺�����
- ��˿�����û��ķ�˿��
- ΢�����ݣ���list����ʽ�洢���û�����΢������
- ΢����Ӧ�ĵ���������list����ʽ�洢���û�����΢����Ӧ�ĵ�����
- ΢����Ӧ��ת��������list����ʽ�洢���û�����΢����Ӧ��ת����
- ΢����Ӧ������������list����ʽ�洢���û�����΢����Ӧ��������
- ����ļ��������ڵ�ǰĿ¼��weibo�ļ��������Ϊ"user_id.txt"����ʽ

### ���л���
- �������ԣ�python2.7
- ϵͳ�� windows 10��64λ��
- ���л�����IPython��Anaconda 64λ��

### ʹ��˵��
1�����ؽű�
```bash
$ git clone https://github.com/dataabc/weibospider.git
```
�����������������Ŀ���ص���ǰĿ¼��������سɹ���ǰĿ¼�����һ����Ϊ"weibospider"���ļ��У�<br>
2�����ı��༭����weibospider�ļ����µ�"weiboSpider.py"�ļ���<br>
3����"weiboSpider.py"�ļ��еġ�your cookie���滻������΢����cookie���������ϸ������λ�ȡcookie��<br>
4����"weiboSpider.py"�ļ��е�user_id�滻����Ҫ��ȡ��΢����user_id���������ϸ������λ�ȡuser_id��<br>
5����������ýű������ű���һ��weibo�࣬�û����԰����Լ����������weibo�ࡣ
�����û�����ֱ����"weiboSpider.py"�ļ��е���weibo�࣬������ô���ʾ�����£�
```python
user_id = 1669879400
filter = 1 
wb = weibo(user_id,filter) #����weibo�࣬����΢��ʵ��wb
wb.start()  #��ȡ΢����Ϣ
```
user_id���Ըĳ�����Ϸ����û�id�������΢��id���⣩��filterĬ��ֵΪ0����ʾ��ȡ����΢����Ϣ��ת��΢��+ԭ��΢������Ϊ1��ʾֻ��ȡ�û�������ԭ��΢����wb��weibo���һ��ʵ����Ҳ�������������֣�ֻҪ����python�������淶���ɣ�ͨ��ִ��wb.start() �����΢������ȡ����������������֮�����ǿ��Եõ��ܶ���Ϣ��<br>
**wb.userName**���û�����<br>
**wb.weiboNum**��΢������<br>
**wb.following**����ע����<br>
**wb.followers**����˿����<br>
**wb.weibos**���洢�û�������΢����Ϊlist��ʽ����filter=1�� wb.weibos[0]Ϊ����һ��**ԭ��**΢����filter=0Ϊ����һ��΢����wb.weibos[1]��wb.weibos[2]�ֱ��ʾ�ڶ��º͵����µ�΢�����Դ����ơ���Ȼ����û�û�з���΢����wb.weibos��Ϊ[]��<br>
**wb.num_zan**���洢΢����õĵ�������Ϊlist��ʽ����wb.num_zan[0]Ϊ����һ��΢����õĵ���������wb.weibos��Ӧ�������÷�ͬwb.weibos��<br>
**wb.num_forwarding**���洢΢����õĵ�������Ϊlist��ʽ����wb.num_forwarding[0]Ϊ����һ��΢����õ�ת��������wb.weibos��Ӧ�������÷�ͬwb.weibos��<br>
**wb.num_comment**���洢΢����õĵ�������Ϊlist��ʽ����wb.num_comment[0]Ϊ����һ��΢����õ�����������wb.weibos��Ӧ�������÷�ͬwb.weibos��<br>
6�����нű����ҵ����л�����IPython,ͨ��
```bash
$ run filepath/weiboSpider.py
```
�������нű�����ҿ��Ը����Լ������л���ѡ�����з�ʽ��

###��λ�ȡcookie
1����Chrome��<https://passport.weibo.cn/signin/login>��<br>
2����F12����Chrome�����߹��ߣ�<br>
3���㿪��Network��������Preserve log��ѡ�У�����΢�����û��������룬��¼����ͼ��ʾ��
![](http://7xknyo.com1.z0.glb.clouddn.com/github/weibospider/cookie1.png)
4�����Chrome�����߹��ߡ�Name"�б��е�"m.weibo.cn",���"Headers"������"Request Headers"�£�"Cookie"���ֵ��Ϊ����Ҫ�ҵ�cookieֵ�����Ƽ��ɣ���ͼ��ʾ��
![](http://7xknyo.com1.z0.glb.clouddn.com/github/weibospider/cookie2.png)

###��λ�ȡuser_id
1������ַ<http://weibo.cn>����������Ҫ�ҵ��ˣ��硱�����á�������������ҳ��<br>
2���󲿷�����£����û���ҳ�ĵ�ַ����Ͱ�����user_id���硱�����á��ĵ�ַ����ַΪ"<http://weibo.cn/u/1729370543?f=search_0>"�����е�"1729370543"��������user_id����ͼ��ʾ��
![](http://7xknyo.com1.z0.glb.clouddn.com/github/weibospider/userid1.png)
���ǲ����û������˸������������ǵĵ�ַ����ַ�ͱ����"<http://weibo.cn/��������?f=search_0>"����ʽ����������ҳ�ĵ�ַ����ַΪ"<http://weibo.cn/guangxianliuyan?f=search_0>"����ͼ��ʾ��
![](http://7xknyo.com1.z0.glb.clouddn.com/github/weibospider/userid2.png)
��ʵ�ϣ����������ȡ΢������user_id��������������ԣ�������Ϊ���ű���Ҫ��ȡ�û��ǳƣ����ø���������ʾ����ҳ��ȡ��һЩС���⣬��Ҫ�������ҳ�����ԣ����������ַ��û��user_id���������ҿ��Ե�������ϡ�����ת���û�����ҳ�棬�����ҵ�����ҳ���ַΪ"<http://weibo.cn/1644461042/info>"�����е�"1644461042"��Ϊ����΢����user_id����ͼ��ʾ��
![](http://7xknyo.com1.z0.glb.clouddn.com/github/weibospider/userid3.png)

###ע������
1��user_id����Ϊ����΢����user_id����ΪҪ��΢����Ϣ�������ȵ�¼��ĳ��΢���˺ţ����˺����ǹ��ҳ�Ϊ����΢��������΢�������Լ���ҳ��ͷ��������û���ҳ�棬�õ�����ҳ��ʽ��ͬ�������޷���ȡ�Լ���΢����Ϣ��<br>
2��cookie���������ƣ���Լ�������ҵ���Ч�ڣ�������Ч�������¸���cookie��