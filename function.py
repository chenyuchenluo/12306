
# -- coding: utf-8 --
# 2.7版本 字符串有两种编码格式（Unicode、utf-8） 防止输出错误

import time 		# 时间
import threading 	# 线程
import requests		# 发送网络请求
import json			# 解析
# import getpass		# 隐藏密码输入
import random 		# 随机数
import os 			# 系统
import platform 	# 设备
import re 			# 正则匹配
from PIL import Image 	# 图片操作
import urllib 		# 用于urldecode

import sys 			# 系统
reload(sys)
sys.setdefaultencoding('utf8')


# 禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 全局
c_js = '@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|2@bjn|北京南|VNP|beijingnan|bjn|3@bjx|北京西|BXP|beijingxi|bjx|4@gzn|广州南|IZQ|guangzhounan|gzn|5@cqb|重庆北|CUW|chongqingbei|cqb|6@cqi|重庆|CQW|chongqing|cq|7@cqn|重庆南|CRW|chongqingnan|cqn|8@cqx|重庆西|CXW|chongqingxi|cqx|9@gzd|广州东|GGQ|guangzhoudong|gzd|10@sha|上海|SHH|shanghai|sh|11@shn|上海南|SNH|shanghainan|shn|12@shq|上海虹桥|AOH|shanghaihongqiao|shhq|13@shx|上海西|SXH|shanghaixi|shx|14@tjb|天津北|TBP|tianjinbei|tjb|15@tji|天津|TJP|tianjin|tj|16@tjn|天津南|TIP|tianjinnan|tjn|17@tjx|天津西|TXP|tianjinxi|tjx|18@cch|长春|CCT|changchun|cc|19@ccn|长春南|CET|changchunnan|ccn|20@ccx|长春西|CRT|changchunxi|ccx|21@cdd|成都东|ICW|chengdudong|cdd|22@cdn|成都南|CNW|chengdunan|cdn|23@cdu|成都|CDW|chengdu|cd|24@csh|长沙|CSQ|changsha|cs|25@csn|长沙南|CWQ|changshanan|csn|26@dmh|大明湖|JAK|daminghu|dmh|27@fzh|福州|FZS|fuzhou|fz|28@fzn|福州南|FYS|fuzhounan|fzn|29@gya|贵阳|GIW|guiyang|gy|30@gzh|广州|GZQ|guangzhou|gz|31@gzx|广州西|GXQ|guangzhouxi|gzx|32@heb|哈尔滨|HBB|haerbin|heb|33@hed|哈尔滨东|VBB|haerbindong|hebd|34@hex|哈尔滨西|VAB|haerbinxi|hebx|35@hfe|合肥|HFH|hefei|hf|36@hfx|合肥西|HTH|hefeixi|hfx|37@hhd|呼和浩特东|NDC|huhehaotedong|hhhtd|38@hht|呼和浩特|HHC|huhehaote|hhht|39@hkd|海口东|KEQ|haikoudong|hkd|40@hkd|海口东|HMQ|haikoudong|hkd|41@hko|海口|VUQ|haikou|hk|42@hzd|杭州东|HGH|hangzhoudong|hzd|43@hzh|杭州|HZH|hangzhou|hz|44@hzn|杭州南|XHH|hangzhounan|hzn|45@jna|济南|JNK|jinan|jn|46@jnx|济南西|JGK|jinanxi|jnx|47@kmi|昆明|KMM|kunming|km|48@kmx|昆明西|KXM|kunmingxi|kmx|49@lsa|拉萨|LSO|lasa|ls|50@lzd|兰州东|LVJ|lanzhoudong|lzd|51@lzh|兰州|LZJ|lanzhou|lz|52@lzx|兰州西|LAJ|lanzhouxi|lzx|53@nch|南昌|NCG|nanchang|nc|54@nji|南京|NJH|nanjing|nj|55@njn|南京南|NKH|nanjingnan|njn|56@nni|南宁|NNZ|nanning|nn|57@sjb|石家庄北|VVP|shijiazhuangbei|sjzb|58@sjz|石家庄|SJP|shijiazhuang|sjz|59@sya|沈阳|SYT|shenyang|sy|60@syb|沈阳北|SBT|shenyangbei|syb|61@syd|沈阳东|SDT|shenyangdong|syd|62@syn|沈阳南|SOT|shenyangnan|syn|63@tyb|太原北|TBV|taiyuanbei|tyb|64@tyd|太原东|TDV|taiyuandong|tyd|65@tyu|太原|TYV|taiyuan|ty|66@wha|武汉|WHN|wuhan|wh|67@wjx|王家营西|KNM|wangjiayingxi|wjyx|68@wln|乌鲁木齐南|WMR|wulumuqinan|wlmqn|69@xab|西安北|EAY|xianbei|xab|70@xan|西安|XAY|xian|xa|71@xan|西安南|CAY|xiannan|xan|72@xni|西宁|XNO|xining|xn|73@ych|银川|YIJ|yinchuan|yc|74@zzh|郑州|ZZF|zhengzhou|zz|75@aes|阿尔山|ART|aershan|aes|76@aka|安康|AKY|ankang|ak|77@aks|阿克苏|ASR|akesu|aks|78@alh|阿里河|AHX|alihe|alh|79@alk|阿拉山口|AKR|alashankou|alsk|80@api|安平|APT|anping|ap|81@aqi|安庆|AQH|anqing|aq|82@ash|安顺|ASW|anshun|as|83@ash|鞍山|AST|anshan|as|84@aya|安阳|AYF|anyang|ay|85@ban|北安|BAB|beian|ba|86@bbu|蚌埠|BBH|bengbu|bb|87@bch|白城|BCT|baicheng|bc|88@bha|北海|BHZ|beihai|bh|89@bhe|白河|BEL|baihe|bh|90@bji|白涧|BAP|baijian|bj|91@bji|宝鸡|BJY|baoji|bj|92@bji|滨江|BJB|binjiang|bj|93@bkt|博克图|BKX|boketu|bkt|94@bse|百色|BIZ|baise|bs|95@bss|白山市|HJL|baishanshi|bss|96@bta|北台|BTT|beitai|bt|97@btd|包头东|BDC|baotoudong|btd|98@bto|包头|BTC|baotou|bt|99@bts|北屯市|BXR|beitunshi|bts|100@bxi|本溪|BXT|benxi|bx|101@byb|白云鄂博|BEC|baiyunebo|byeb|102@byx|白银西|BXJ|baiyinxi|byx|103@bzh|亳州|BZH|bozhou|bz|104@cbi|赤壁|CBN|chibi|cb|105@cde|常德|VGQ|changde|cd|106@cde|承德|CDP|chengde|cd|107@cdi|长甸|CDT|changdian|cd|108@cfe|赤峰|CFD|chifeng|cf|109@cli|茶陵|CDG|chaling|cl|110@cna|苍南|CEH|cangnan|cn|111@cpi|昌平|CPP|changping|cp|112@cre|崇仁|CRG|chongren|cr|113@ctu|昌图|CTT|changtu|ct|114@ctz|长汀镇|CDB|changtingzhen|ctz|115@cxi|曹县|CXK|caoxian|cx|116@cxn|楚雄南|COM|chuxiongnan|cxn|117@cxt|陈相屯|CXT|chenxiangtun|cxt|118@czb|长治北|CBF|changzhibei|czb|119@czh|池州|IYH|chizhou|cz|120@czh|长征|CZJ|changzheng|cz|121@czh|常州|CZH|changzhou|cz|122@czh|郴州|CZQ|chenzhou|cz|123@czh|长治|CZF|changzhi|cz|124@czh|沧州|COP|cangzhou|cz|125@czu|崇左|CZZ|chongzuo|cz|126@dab|大安北|RNT|daanbei|dab|127@dch|大成|DCT|dacheng|dc|128@ddo|丹东|DUT|dandong|dd|129@dfh|东方红|DFB|dongfanghong|dfh|130@dgd|东莞东|DMQ|dongguandong|dgd|131@dhs|大虎山|DHD|dahushan|dhs|132@dhu|敦化|DHL|dunhua|dh|133@dhu|敦煌|DHJ|dunhuang|dh|134@dhu|德惠|DHT|dehui|dh|135@djc|东京城|DJB|dongjingcheng|djc|136@dji|大涧|DFP|dajian|dj|137@djy|都江堰|DDW|dujiangyan|djy|138@dlb|大连北|DFT|dalianbei|dlb|139@dli|大理|DKM|dali|dl|140@dli|大连|DLT|dalian|dl|141@dna|定南|DNG|dingnan|dn|142@dqi|大庆|DZX|daqing|dq|143@dsh|东胜|DOC|dongsheng|ds|144@dsq|大石桥|DQT|dashiqiao|dsq|145@dto|大同|DTV|datong|dt|146@dyi|东营|DPK|dongying|dy|147@dys|大杨树|DUX|dayangshu|dys|148@dyu|都匀|RYW|duyun|dy|149@dzh|邓州|DOF|dengzhou|dz|150@dzh|达州|RXW|dazhou|dz|151@dzh|德州|DZP|dezhou|dz|152@ejn|额济纳|EJC|ejina|ejn|153@eli|二连|RLC|erlian|el|154@esh|恩施|ESN|enshi|es|155@fdi|福鼎|FES|fuding|fd|156@fhc|凤凰机场|FJQ|fenghuangjichang|fhjc|157@fld|风陵渡|FLV|fenglingdu|fld|158@fli|涪陵|FLW|fuling|fl|159@flj|富拉尔基|FRX|fulaerji|flej|160@fsb|抚顺北|FET|fushunbei|fsb|161@fsh|佛山|FSQ|foshan|fs|162@fxn|阜新南|FXD|fuxinnan|fxn|163@fya|阜阳|FYH|fuyang|fy|164@gem|格尔木|GRO|geermu|gem|165@gha|广汉|GHW|guanghan|gh|166@gji|古交|GJV|gujiao|gj|167@glb|桂林北|GBZ|guilinbei|glb|168@gli|古莲|GRX|gulian|gl|169@gli|桂林|GLZ|guilin|gl|170@gsh|固始|GXN|gushi|gs|171@gsh|广水|GSN|guangshui|gs|172@gta|干塘|GNJ|gantang|gt|173@gyu|广元|GYW|guangyuan|gy|174@gzb|广州北|GBQ|guangzhoubei|gzb|175@gzh|赣州|GZG|ganzhou|gz|176@gzl|公主岭|GLT|gongzhuling|gzl|177@gzn|公主岭南|GBT|gongzhulingnan|gzln|178@han|淮安|AUH|huaian|ha|179@hbe|淮北|HRH|huaibei|hb|180@hbe|鹤北|HMB|hebei|hb|181@hbi|淮滨|HVN|huaibin|hb|182@hbi|河边|HBV|hebian|hb|183@hch|潢川|KCN|huangchuan|hc|184@hch|韩城|HCY|hancheng|hc|185@hda|邯郸|HDP|handan|hd|186@hdz|横道河子|HDB|hengdaohezi|hdhz|187@hga|鹤岗|HGB|hegang|hg|188@hgt|皇姑屯|HTT|huanggutun|hgt|189@hgu|红果|HEM|hongguo|hg|190@hhe|黑河|HJB|heihe|hh|191@hhu|怀化|HHQ|huaihua|hh|192@hko|汉口|HKN|hankou|hk|193@hld|葫芦岛|HLD|huludao|hld|194@hle|海拉尔|HRX|hailaer|hle|195@hll|霍林郭勒|HWD|huolinguole|hlgl|196@hlu|海伦|HLB|hailun|hl|197@hma|侯马|HMV|houma|hm|198@hmi|哈密|HMR|hami|hm|199@hna|淮南|HAH|huainan|hn|200@hna|桦南|HNB|huanan|hn|201@hnx|海宁西|EUH|hainingxi|hnx|202@hqi|鹤庆|HQM|heqing|hq|203@hrb|怀柔北|HBP|huairoubei|hrb|204@hro|怀柔|HRP|huairou|hr|205@hsd|黄石东|OSN|huangshidong|hsd|206@hsh|华山|HSY|huashan|hs|207@hsh|黄山|HKH|huangshan|hs|208@hsh|黄石|HSN|huangshi|hs|209@hsh|衡水|HSP|hengshui|hs|210@hya|衡阳|HYQ|hengyang|hy|211@hze|菏泽|HIK|heze|hz|212@hzh|贺州|HXZ|hezhou|hz|213@hzh|汉中|HOY|hanzhong|hz|214@hzh|惠州|HCQ|huizhou|hz|215@jan|吉安|VAG|jian|ja|216@jan|集安|JAL|jian|ja|217@jbc|江边村|JBG|jiangbiancun|jbc|218@jch|晋城|JCF|jincheng|jc|219@jcj|金城江|JJZ|jinchengjiang|jcj|220@jdz|景德镇|JCG|jingdezhen|jdz|221@jfe|嘉峰|JFF|jiafeng|jf|222@jgq|加格达奇|JGX|jiagedaqi|jgdq|223@jgs|井冈山|JGG|jinggangshan|jgs|224@jhe|蛟河|JHL|jiaohe|jh|225@jhn|金华南|RNH|jinhuanan|jhn|226@jhu|金华|JBH|jinhua|jh|227@jji|九江|JJG|jiujiang|jj|228@jli|吉林|JLL|jilin|jl|229@jme|荆门|JMN|jingmen|jm|230@jms|佳木斯|JMB|jiamusi|jms|231@jni|济宁|JIK|jining|jn|232@jnn|集宁南|JAC|jiningnan|jnn|233@jqu|酒泉|JQJ|jiuquan|jq|234@jsh|江山|JUH|jiangshan|js|235@jsh|吉首|JIQ|jishou|js|236@jta|九台|JTL|jiutai|jt|237@jts|镜铁山|JVJ|jingtieshan|jts|238@jxi|鸡西|JXB|jixi|jx|239@jxx|绩溪县|JRH|jixixian|jxx|240@jyg|嘉峪关|JGJ|jiayuguan|jyg|241@jyo|江油|JFW|jiangyou|jy|242@jzh|金州|JZT|jinzhou|jz|243@jzh|锦州|JZD|jinzhou|jz|244@jzh|蓟州|JKP|jizhou|jz|245@kel|库尔勒|KLR|kuerle|kel|246@kfe|开封|KFF|kaifeng|kf|247@kla|岢岚|KLV|kelan|kl|248@kli|凯里|KLW|kaili|kl|249@ksh|喀什|KSR|kashi|ks|250@ksn|昆山南|KNH|kunshannan|ksn|251@ktu|奎屯|KTR|kuitun|kt|252@kyu|开原|KYT|kaiyuan|ky|253@lan|六安|UAH|luan|la|254@lba|灵宝|LBF|lingbao|lb|255@lcg|芦潮港|UCH|luchaogang|lcg|256@lch|隆昌|LCW|longchang|lc|257@lch|陆川|LKZ|luchuan|lc|258@lch|利川|LCN|lichuan|lc|259@lch|临川|LCG|linchuan|lc|260@lch|潞城|UTP|lucheng|lc|261@lda|鹿道|LDL|ludao|ld|262@ldi|娄底|LDQ|loudi|ld|263@lfe|临汾|LFV|linfen|lf|264@lgz|良各庄|LGP|lianggezhuang|lgz|265@lhe|临河|LHC|linhe|lh|266@lhe|漯河|LON|luohe|lh|267@lhu|绿化|LWJ|lvhua|lh|268@lhu|隆化|UHP|longhua|lh|269@lji|丽江|LHM|lijiang|lj|270@lji|临江|LQL|linjiang|lj|271@lji|龙井|LJL|longjing|lj|272@lli|吕梁|LHV|lvliang|ll|273@lli|醴陵|LLG|liling|ll|274@lln|柳林南|LKV|liulinnan|lln|275@lpi|滦平|UPP|luanping|lp|276@lps|六盘水|UMW|liupanshui|lps|277@lqi|灵丘|LVV|lingqiu|lq|278@lsh|旅顺|LST|lvshun|ls|279@lxi|兰溪|LWH|lanxi|lx|280@lxi|陇西|LXJ|longxi|lx|281@lxi|澧县|LEQ|lixian|lx|282@lxi|临西|UEP|linxi|lx|283@lya|龙岩|LYS|longyan|ly|284@lya|耒阳|LYQ|leiyang|ly|285@lya|洛阳|LYF|luoyang|ly|286@lyd|连云港东|UKH|lianyungangdong|lygd|287@lyd|洛阳东|LDF|luoyangdong|lyd|288@lyi|临沂|LVK|linyi|ly|289@lym|洛阳龙门|LLF|luoyanglongmen|lylm|290@lyu|柳园|DHR|liuyuan|ly|291@lyu|凌源|LYD|lingyuan|ly|292@lyu|辽源|LYL|liaoyuan|ly|293@lzh|立志|LZX|lizhi|lz|294@lzh|柳州|LZZ|liuzhou|lz|295@lzh|辽中|LZD|liaozhong|lz|296@mch|麻城|MCN|macheng|mc|297@mdh|免渡河|MDX|mianduhe|mdh|298@mdj|牡丹江|MDB|mudanjiang|mdj|299@meg|莫尔道嘎|MRX|moerdaoga|medg|300@mgu|明光|MGH|mingguang|mg|301@mgu|满归|MHX|mangui|mg|302@mhe|漠河|MVX|mohe|mh|303@mmi|茂名|MDQ|maoming|mm|304@mmx|茂名西|MMZ|maomingxi|mmx|305@msh|密山|MSB|mishan|ms|306@msj|马三家|MJT|masanjia|msj|307@mwe|麻尾|VAW|mawei|mw|308@mya|绵阳|MYW|mianyang|my|309@mzh|梅州|MOQ|meizhou|mz|310@mzl|满洲里|MLX|manzhouli|mzl|311@nbd|宁波东|NVH|ningbodong|nbd|312@nbo|宁波|NGH|ningbo|nb|313@nch|南岔|NCB|nancha|nc|314@nch|南充|NCW|nanchong|nc|315@nda|南丹|NDZ|nandan|nd|316@ndm|南大庙|NMP|nandamiao|ndm|317@nfe|南芬|NFT|nanfen|nf|318@nhe|讷河|NHX|nehe|nh|319@nji|嫩江|NGX|nenjiang|nj|320@nji|内江|NJW|neijiang|nj|321@npi|南平|NPS|nanping|np|322@nto|南通|NUH|nantong|nt|323@nya|南阳|NFF|nanyang|ny|324@nzs|碾子山|NZX|nianzishan|nzs|325@pds|平顶山|PEN|pingdingshan|pds|326@pji|盘锦|PVD|panjin|pj|327@pli|平凉|PIJ|pingliang|pl|328@pln|平凉南|POJ|pingliangnan|pln|329@pqu|平泉|PQP|pingquan|pq|330@psh|坪石|PSQ|pingshi|ps|331@pxi|萍乡|PXG|pingxiang|px|332@pxi|凭祥|PXZ|pingxiang|px|333@pxx|郫县西|PCW|pixianxi|pxx|334@pzh|攀枝花|PRW|panzhihua|pzh|335@qch|蕲春|QRN|qichun|qc|336@qcs|青城山|QSW|qingchengshan|qcs|337@qda|青岛|QDK|qingdao|qd|338@qhc|清河城|QYP|qinghecheng|qhc|339@qji|曲靖|QJM|qujing|qj|340@qji|黔江|QNW|qianjiang|qj|341@qjz|前进镇|QEB|qianjinzhen|qjz|342@qqe|齐齐哈尔|QHX|qiqihaer|qqhe|343@qth|七台河|QTB|qitaihe|qth|344@qxi|沁县|QVV|qinxian|qx|345@qzd|泉州东|QRS|quanzhoudong|qzd|346@qzh|泉州|QYS|quanzhou|qz|347@qzh|衢州|QEH|quzhou|qz|348@ran|融安|RAZ|rongan|ra|349@rjg|汝箕沟|RQJ|rujigou|rjg|350@rji|瑞金|RJG|ruijin|rj|351@rzh|日照|RZK|rizhao|rz|352@scp|双城堡|SCB|shuangchengpu|scp|353@sfh|绥芬河|SFB|suifenhe|sfh|354@sgd|韶关东|SGQ|shaoguandong|sgd|355@shg|山海关|SHD|shanhaiguan|shg|356@shu|绥化|SHB|suihua|sh|357@sjf|三间房|SFX|sanjianfang|sjf|358@sjt|苏家屯|SXT|sujiatun|sjt|359@sla|舒兰|SLL|shulan|sl|360@smn|神木南|OMY|shenmunan|smn|361@smx|三门峡|SMF|sanmenxia|smx|362@sna|商南|ONY|shangnan|sn|363@sni|遂宁|NIW|suining|sn|364@spi|四平|SPT|siping|sp|365@sqi|商丘|SQF|shangqiu|sq|366@sra|上饶|SRG|shangrao|sr|367@ssh|韶山|SSQ|shaoshan|ss|368@sso|宿松|OAH|susong|ss|369@sto|汕头|OTQ|shantou|st|370@swu|邵武|SWS|shaowu|sw|371@sxi|涉县|OEP|shexian|sx|372@sya|三亚|SEQ|sanya|sy|373@sya|三  亚|JUQ|sanya|sya|374@sya|邵阳|SYQ|shaoyang|sy|375@sya|十堰|SNN|shiyan|sy|376@syq|三元区|SMS|sanyuanqu|syq|377@sys|双鸭山|SSB|shuangyashan|sys|378@syu|松原|VYT|songyuan|sy|379@szh|苏州|SZH|suzhou|sz|380@szh|深圳|SZQ|shenzhen|sz|381@szh|宿州|OXH|suzhou|sz|382@szh|随州|SZN|suizhou|sz|383@szh|朔州|SUV|shuozhou|sz|384@szx|深圳西|OSQ|shenzhenxi|szx|385@tba|塘豹|TBQ|tangbao|tb|386@teq|塔尔气|TVX|taerqi|teq|387@tgu|潼关|TGY|tongguan|tg|388@tgu|塘沽|TGP|tanggu|tg|389@the|塔河|TXX|tahe|th|390@thu|通化|THL|tonghua|th|391@tla|泰来|TLX|tailai|tl|392@tlf|吐鲁番|TFR|tulufan|tlf|393@tli|通辽|TLD|tongliao|tl|394@tli|铁岭|TLT|tieling|tl|395@tlz|陶赖昭|TPT|taolaizhao|tlz|396@tme|图们|TML|tumen|tm|397@tre|铜仁|RDQ|tongren|tr|398@tsb|唐山北|FUP|tangshanbei|tsb|399@tsf|田师府|TFT|tianshifu|tsf|400@tsh|泰山|TAK|taishan|ts|401@tsh|唐山|TSP|tangshan|ts|402@tsh|天水|TSJ|tianshui|ts|403@typ|通远堡|TYT|tongyuanpu|typ|404@tys|太阳升|TQT|taiyangsheng|tys|405@tzh|泰州|UTH|taizhou|tz|406@tzi|桐梓|TZW|tongzi|tz|407@tzx|通州西|TAP|tongzhouxi|tzx|408@wch|五常|WCB|wuchang|wc|409@wch|武昌|WCN|wuchang|wc|410@wfd|瓦房店|WDT|wafangdian|wfd|411@wha|威海|WKK|weihai|wh|412@whu|芜湖|WHH|wuhu|wh|413@whx|乌海西|WXC|wuhaixi|whx|414@wjt|吴家屯|WJT|wujiatun|wjt|415@wlo|武隆|WLW|wulong|wl|416@wlt|乌兰浩特|WWT|wulanhaote|wlht|417@wna|渭南|WNY|weinan|wn|418@wsh|威舍|WSM|weishe|ws|419@wts|歪头山|WIT|waitoushan|wts|420@wwe|武威|WUJ|wuwei|ww|421@wwn|武威南|WWJ|wuweinan|wwn|422@wxi|无锡|WXH|wuxi|wx|423@wxi|乌西|WXR|wuxi|wx|424@wyl|乌伊岭|WPB|wuyiling|wyl|425@wys|武夷山|WAS|wuyishan|wys|426@wyu|万源|WYY|wanyuan|wy|427@wzh|万州|WYW|wanzhou|wz|428@wzh|梧州|WZZ|wuzhou|wz|429@wzh|温州|RZH|wenzhou|wz|430@wzn|温州南|VRH|wenzhounan|wzn|431@xch|西昌|ECW|xichang|xc|432@xch|许昌|XCF|xuchang|xc|433@xcn|西昌南|ENW|xichangnan|xcn|434@xfa|香坊|XFB|xiangfang|xf|435@xga|轩岗|XGV|xuangang|xg|436@xgu|兴国|EUG|xingguo|xg|437@xha|宣汉|XHY|xuanhan|xh|438@xhu|新会|EFQ|xinhui|xh|439@xhu|新晃|XLQ|xinhuang|xh|440@xlt|锡林浩特|XTC|xilinhaote|xlht|441@xlx|兴隆县|EXP|xinglongxian|xlx|442@xmb|厦门北|XKS|xiamenbei|xmb|443@xme|厦门|XMS|xiamen|xm|444@xmq|厦门高崎|XBS|xiamengaoqi|xmgq|445@xsh|小市|XST|xiaoshi|xs|446@xsh|秀山|ETW|xiushan|xs|447@xta|向塘|XTG|xiangtang|xt|448@xwe|宣威|XWM|xuanwei|xw|449@xxi|新乡|XXF|xinxiang|xx|450@xya|信阳|XUN|xinyang|xy|451@xya|咸阳|XYY|xianyang|xy|452@xya|襄阳|XFN|xiangyang|xy|453@xyc|熊岳城|XYT|xiongyuecheng|xyc|454@xyi|新沂|VIH|xinyi|xy|455@xyi|兴义|XRZ|xingyi|xy|456@xyu|新余|XUG|xinyu|xy|457@xzh|徐州|XCH|xuzhou|xz|458@yan|延安|YWY|yanan|ya|459@ybi|宜宾|YBW|yibin|yb|460@ybn|亚布力南|YWB|yabulinan|ybln|461@ybs|叶柏寿|YBD|yebaishou|ybs|462@ycd|宜昌东|HAN|yichangdong|ycd|463@ych|永川|YCW|yongchuan|yc|464@ych|盐城|AFH|yancheng|yc|465@ych|宜昌|YCN|yichang|yc|466@ych|运城|YNV|yuncheng|yc|467@ych|伊春|YCB|yichun|yc|468@yci|榆次|YCV|yuci|yc|469@ycu|杨村|YBP|yangcun|yc|470@ycx|宜春西|YCG|yichunxi|ycx|471@yes|伊尔施|YET|yiershi|yes|472@yga|燕岗|YGW|yangang|yg|473@yji|永济|YIV|yongji|yj|474@yji|延吉|YJL|yanji|yj|475@yko|营口|YKT|yingkou|yk|476@yks|牙克石|YKX|yakeshi|yks|477@yli|阎良|YNY|yanliang|yl|478@yli|玉林|YLZ|yulin|yl|479@yli|榆林|ALY|yulin|yl|480@ylw|亚龙湾|TWQ|yalongwan|ylw|481@ymp|一面坡|YPB|yimianpo|ymp|482@yni|伊宁|YMR|yining|yn|483@ypg|阳平关|YAY|yangpingguan|ypg|484@ypi|玉屏|YZW|yuping|yp|485@ypi|原平|YPV|yuanping|yp|486@yqi|延庆|YNP|yanqing|yq|487@yqq|阳泉曲|YYV|yangquanqu|yqq|488@yqu|玉泉|YQB|yuquan|yq|489@yqu|阳泉|AQP|yangquan|yq|490@ysh|营山|NUW|yingshan|ys|491@ysh|玉山|YNG|yushan|ys|492@ysh|燕山|AOP|yanshan|ys|493@ysh|榆树|YRT|yushu|ys|494@yta|鹰潭|YTG|yingtan|yt|495@yta|烟台|YAK|yantai|yt|496@yth|伊图里河|YEX|yitulihe|ytlh|497@ytx|玉田县|ATP|yutianxian|ytx|498@ywu|义乌|YWH|yiwu|yw|499@yxi|阳新|YON|yangxin|yx|500@yxi|义县|YXD|yixian|yx|501@yya|益阳|AEQ|yiyang|yy|502@yya|岳阳|YYQ|yueyang|yy|503@yzh|崖州|YUQ|yazhou|yz|504@yzh|永州|AOQ|yongzhou|yz|505@yzh|扬州|YLH|yangzhou|yz|506@zbo|淄博|ZBK|zibo|zb|507@zcd|镇城底|ZDV|zhenchengdi|zcd|508@zgo|自贡|ZGW|zigong|zg|509@zha|珠海|ZHQ|zhuhai|zh|510@zhb|珠海北|ZIQ|zhuhaibei|zhb|511@zji|湛江|ZJZ|zhanjiang|zj|512@zji|镇江|ZJH|zhenjiang|zj|513@zjj|张家界|DIQ|zhangjiajie|zjj|514@zjk|张家口|ZKP|zhangjiakou|zjk|515@zjn|张家口南|ZMP|zhangjiakounan|zjkn|516@zko|周口|ZKN|zhoukou|zk|517@zlm|哲里木|ZLC|zhelimu|zlm|518@zlt|扎兰屯|ZTX|zhalantun|zlt|519@zmd|驻马店|ZDN|zhumadian|zmd|520@zqi|肇庆|ZVQ|zhaoqing|zq|521@zsz|周水子|ZIT|zhoushuizi|zsz|522@zto|昭通|ZDW|zhaotong|zt|523@zwe|中卫|ZWJ|zhongwei|zw|524@zya|资阳|ZYW|ziyang|zy|525@zyx|遵义西|ZIW|zunyixi|zyx|526@zzh|枣庄|ZEK|zaozhuang|zz|527@zzh|资中|ZZW|zizhong|zz|528@zzh|株洲|ZZQ|zhuzhou|zz|529@zzx|枣庄西|ZFK|zaozhuangxi|zzx|530@aax|昂昂溪|AAX|angangxi|aax|531@ach|阿城|ACB|acheng|ac|532@ada|安达|ADX|anda|ad|533@ade|安德|ARW|ande|ad|534@adi|安定|ADP|anding|ad|535@adu|安多|ADO|anduo|ad|536@agu|安广|AGT|anguang|ag|537@aha|敖汉|YED|aohan|ah|538@ahe|艾河|AHP|aihe|ah|539@ahu|安化|PKQ|anhua|ah|540@ajc|艾家村|AJJ|aijiacun|ajc|541@aji|鳌江|ARH|aojiang|aj|542@aji|安家|AJB|anjia|aj|543@aji|阿金|AJD|ajin|aj|544@aji|安靖|PYW|anjing|aj|545@akt|阿克陶|AER|aketao|akt|546@aky|安口窑|AYY|ankouyao|aky|547@alg|敖力布告|ALD|aolibugao|albg|548@alo|安龙|AUZ|anlong|al|549@als|阿龙山|ASX|alongshan|als|550@alu|安陆|ALN|anlu|al|551@ame|阿木尔|JTX|amuer|ame|552@anz|阿南庄|AZM|ananzhuang|anz|553@aqx|安庆西|APH|anqingxi|aqx|554@asx|鞍山西|AXT|anshanxi|asx|555@ata|安塘|ATV|antang|at|556@atb|安亭北|ASH|antingbei|atb|557@ats|阿图什|ATR|atushi|ats|558@atu|安图|ATL|antu|at|559@axi|安溪|AXS|anxi|ax|560@bao|博鳌|BWQ|boao|ba|561@bbe|北碚|BPW|beibei|bb|562@bbg|白壁关|BGV|baibiguan|bbg|563@bbn|蚌埠南|BMH|bengbunan|bbn|564@bch|巴楚|BCR|bachu|bc|565@bch|板城|BUP|bancheng|bc|566@bdh|北戴河|BEP|beidaihe|bdh|567@bdi|保定|BDP|baoding|bd|568@bdi|宝坻|BPP|baodi|bd|569@bdl|八达岭|ILP|badaling|bdl|570@bdo|巴东|BNN|badong|bd|571@bgu|柏果|BGM|baiguo|bg|572@bha|布海|BUT|buhai|bh|573@bhd|白河东|BIY|baihedong|bhd|574@bho|贲红|BVC|benhong|bh|575@bhs|宝华山|BWH|baohuashan|bhs|576@bhx|白河县|BEY|baihexian|bhx|577@bjg|白芨沟|BJJ|baijigou|bjg|578@bjg|碧鸡关|BJM|bijiguan|bjg|579@bji|北滘|IBQ|beijiao|bj|580@bji|碧江|BLQ|bijiang|bj|581@bjp|白鸡坡|BBM|baijipo|bjp|582@bjs|笔架山|BSB|bijiashan|bjs|583@bjt|八角台|BTD|bajiaotai|bjt|584@bka|保康|BKD|baokang|bk|585@bkp|白奎堡|BKB|baikuipu|bkp|586@bla|白狼|BAT|bailang|bl|587@bla|百浪|BRZ|bailang|bl|588@ble|博乐|BOR|bole|bl|589@blg|宝拉格|BQC|baolage|blg|590@bli|巴林|BLX|balin|bl|591@bli|宝林|BNB|baolin|bl|592@bli|北流|BOZ|beiliu|bl|593@bli|勃利|BLB|boli|bl|594@blk|布列开|BLR|buliekai|blk|595@bls|宝龙山|BND|baolongshan|bls|596@blx|百里峡|AAP|bailixia|blx|597@bmc|八面城|BMD|bamiancheng|bmc|598@bmq|班猫箐|BNM|banmaoqing|bmq|599@bmt|八面通|BMB|bamiantong|bmt|600@bmz|北马圈子|BRP|beimaquanzi|bmqz|601@bpn|北票南|RPD|beipiaonan|bpn|602@bqi|白旗|BQP|baiqi|bq|603@bql|宝泉岭|BQB|baoquanling|bql|604@bqu|白泉|BQL|baiquan|bq|605@bsh|巴山|BAY|bashan|bs|606@bsj|白水江|BSY|baishuijiang|bsj|607@bsp|白沙坡|BPM|baishapo|bsp|608@bss|白石山|BAL|baishishan|bss|609@bsz|白水镇|BUM|baishuizhen|bsz|610@btd|包头 东|FDC|baotoudong|btd|611@bti|坂田|BTQ|bantian|bt|612@bto|泊头|BZP|botou|bt|613@btu|北屯|BYP|beitun|bt|614@bxh|本溪湖|BHT|benxihu|bxh|615@bxi|博兴|BXK|boxing|bx|616@bxt|八仙筒|VXD|baxiantong|bxt|617@byg|白音察干|BYC|baiyinchagan|bycg|618@byh|背荫河|BYB|beiyinhe|byh|619@byi|北营|BIV|beiying|by|620@byl|巴彦高勒|BAC|bayangaole|bygl|621@byl|白音他拉|BID|baiyintala|bytl|622@byq|鲅鱼圈|BYT|bayuquan|byq|623@bys|白银市|BNJ|baiyinshi|bys|624@bys|白音胡硕|BCD|baiyinhushuo|byhs|625@bzh|巴中|IEW|bazhong|bz|626@bzh|霸州|RMP|bazhou|bz|627@bzh|北宅|BVP|beizhai|bz|628@cbb|赤壁北|CIN|chibibei|cbb|629@cbg|查布嘎|CBC|chabuga|cbg|630@cch|长城|CEJ|changcheng|cc|631@cch|长冲|CCM|changchong|cc|632@cdd|承德东|CCP|chengdedong|cdd|633@cfx|赤峰西|CID|chifengxi|cfx|634@cga|嵯岗|CAX|cuogang|cg|635@cga|柴岗|CGT|chaigang|cg|636@cge|长葛|CEF|changge|cg|637@cgp|柴沟堡|CGV|chaigoupu|cgp|638@cgu|城固|CGY|chenggu|cg|639@cgy|陈官营|CAJ|chenguanying|cgy|640@cgz|成高子|CZB|chenggaozi|cgz|641@cha|草海|WBW|caohai|ch|642@che|柴河|CHB|chaihe|ch|643@che|册亨|CHZ|ceheng|ch|644@chk|草河口|CKT|caohekou|chk|645@chk|崔黄口|CHP|cuihuangkou|chk|646@chu|巢湖|CIH|chaohu|ch|647@cjg|蔡家沟|CJT|caijiagou|cjg|648@cjh|成吉思汗|CJX|chengjisihan|cjsh|649@cji|岔江|CAM|chajiang|cj|650@cjp|蔡家坡|CJY|caijiapo|cjp|651@cle|昌乐|CLK|changle|cl|652@clg|超梁沟|CYP|chaolianggou|clg|653@cli|慈利|CUQ|cili|cl|654@cli|昌黎|CLP|changli|cl|655@clz|长岭子|CLT|changlingzi|clz|656@cmi|晨明|CMB|chenming|cm|657@cno|长农|CNJ|changnong|cn|658@cpb|昌平北|VBP|changpingbei|cpb|659@cpi|常平|DAQ|changping|cp|660@cpl|长坡岭|CPM|changpoling|cpl|661@cqi|辰清|CQB|chenqing|cq|662@csh|蔡山|CON|caishan|cs|663@csh|楚山|CSB|chushan|cs|664@csh|长寿|EFW|changshou|cs|665@csh|磁山|CSP|cishan|cs|666@csh|苍石|CST|cangshi|cs|667@csh|草市|CSL|caoshi|cs|668@csq|察素齐|CSC|chasuqi|csq|669@cst|长山屯|CVT|changshantun|cst|670@cti|长汀|CES|changting|ct|671@ctn|朝天南|CTY|chaotiannan|ctn|672@ctx|昌图西|CPT|changtuxi|ctx|673@cwa|春湾|CQQ|chunwan|cw|674@cxi|磁县|CIP|cixian|cx|675@cxi|岑溪|CNZ|cenxi|cx|676@cxi|辰溪|CXQ|chenxi|cx|677@cxi|磁西|CRP|cixi|cx|678@cxn|长兴南|CFH|changxingnan|cxn|679@cya|磁窑|CYK|ciyao|cy|680@cya|春阳|CAL|chunyang|cy|681@cya|城阳|CEK|chengyang|cy|682@cyc|创业村|CEX|chuangyecun|cyc|683@cyc|朝阳川|CYL|chaoyangchuan|cyc|684@cyd|朝阳地|CDD|chaoyangdi|cyd|685@cyn|朝阳南|CYD|chaoyangnan|cyn|686@cyu|长垣|CYF|changyuan|cy|687@cyz|朝阳镇|CZL|chaoyangzhen|cyz|688@czb|滁州北|CUH|chuzhoubei|czb|689@czb|常州北|ESH|changzhoubei|czb|690@czh|滁州|CXH|chuzhou|cz|691@czh|潮州|CKQ|chaozhou|cz|692@czh|常庄|CVK|changzhuang|cz|693@czl|曹子里|CFP|caozili|czl|694@czw|车转湾|CWM|chezhuanwan|czw|695@czx|郴州西|ICQ|chenzhouxi|czx|696@czx|沧州西|CBP|cangzhouxi|czx|697@dan|德安|DAG|dean|da|698@dan|大安|RAT|daan|da|699@dba|大坝|DBJ|daba|db|700@dba|大板|DBC|daban|db|701@dba|大巴|DBD|daba|db|702@dba|电白|NWQ|dianbai|db|703@dba|到保|RBT|daobao|db|704@dbi|定边|DYJ|dingbian|db|705@dbj|东边井|DBB|dongbianjing|dbj|706@dbs|德伯斯|RDT|debosi|dbs|707@dcg|打柴沟|DGJ|dachaigou|dcg|708@dch|德昌|DVW|dechang|dc|709@dda|滴道|DDB|didao|dd|710@ddg|大磴沟|DKJ|dadenggou|ddg|711@ded|刀尔登|DRD|daoerdeng|ded|712@dee|得耳布尔|DRX|deerbuer|debe|713@det|杜尔伯特|TKX|duerbote|debt|714@dfa|东方|UFQ|dongfang|df|715@dfe|丹凤|DGY|danfeng|df|716@dfe|东丰|DIL|dongfeng|df|717@dge|都格|DMM|duge|dg|718@dgt|大官屯|DTT|daguantun|dgt|719@dgu|大关|RGW|daguan|dg|720@dgu|东光|DGP|dongguang|dg|721@dha|东海|DHB|donghai|dh|722@dhc|大灰厂|DHP|dahuichang|dhc|723@dhq|大红旗|DQD|dahongqi|dhq|724@dht|大禾塘|SOQ|shaodong|dh|725@dhx|德惠西|DXT|dehuixi|dhx|726@dhx|东海县|DQH|donghaixian|dhx|727@djg|达家沟|DJT|dajiagou|djg|728@dji|东津|DKB|dongjin|dj|729@dji|杜家|DJL|dujia|dj|730@dkt|大口屯|DKP|dakoutun|dkt|731@dla|东来|RVD|donglai|dl|732@dlh|德令哈|DHO|delingha|dlh|733@dlh|大陆号|DLC|daluhao|dlh|734@dli|带岭|DLB|dailing|dl|735@dli|大林|DLD|dalin|dl|736@dlq|达拉特旗|DIC|dalateqi|dltq|737@dlt|独立屯|DTX|dulitun|dlt|738@dlu|豆罗|DLV|douluo|dl|739@dlx|达拉特西|DNC|dalatexi|dltx|740@dlx|大连西|GZT|dalianxi|dlx|741@dmc|东明村|DMD|dongmingcun|dmc|742@dmh|洞庙河|DEP|dongmiaohe|dmh|743@dmx|东明县|DNF|dongmingxian|dmx|744@dni|大拟|DNZ|dani|dn|745@dpf|大平房|DPD|dapingfang|dpf|746@dps|大盘石|RPP|dapanshi|dps|747@dpu|大埔|DPI|dapu|dp|748@dpu|大堡|DVT|dapu|dp|749@dqd|大庆东|LFX|daqingdong|dqd|750@dqh|大其拉哈|DQX|daqilaha|dqlh|751@dqi|道清|DML|daoqing|dq|752@dqs|对青山|DQB|duiqingshan|dqs|753@dqx|德清西|MOH|deqingxi|dqx|754@dqx|大庆西|RHX|daqingxi|dqx|755@dsh|东升|DRQ|dongsheng|ds|756@dsh|砀山|DKH|dangshan|ds|757@dsh|独山|RWW|dushan|ds|758@dsh|登沙河|DWT|dengshahe|dsh|759@dsp|读书铺|DPM|dushupu|dsp|760@dst|大石头|DSL|dashitou|dst|761@dsx|东胜西|DYC|dongshengxi|dsx|762@dsz|大石寨|RZT|dashizhai|dsz|763@dta|东台|DBH|dongtai|dt|764@dta|定陶|DQK|dingtao|dt|765@dta|灯塔|DGT|dengta|dt|766@dtb|大田边|DBM|datianbian|dtb|767@dth|东通化|DTL|dongtonghua|dth|768@dtu|丹徒|RUH|dantu|dt|769@dtu|大屯|DNT|datun|dt|770@dwa|东湾|DRJ|dongwan|dw|771@dwk|大武口|DFJ|dawukou|dwk|772@dwp|低窝铺|DWJ|diwopu|dwp|773@dwt|大王滩|DZZ|dawangtan|dwt|774@dwz|大湾子|DFM|dawanzi|dwz|775@dxg|大兴沟|DXL|daxinggou|dxg|776@dxi|大兴|DXX|daxing|dx|777@dxi|定西|DSJ|dingxi|dx|778@dxi|甸心|DXM|dianxin|dx|779@dxi|东乡|DXG|dongxiang|dx|780@dxi|代县|DKV|daixian|dx|781@dxi|定襄|DXV|dingxiang|dx|782@dxu|东戌|RXP|dongxu|dx|783@dxz|东辛庄|DXD|dongxinzhuang|dxz|784@dya|丹阳|DYH|danyang|dy|785@dya|德阳|DYW|deyang|dy|786@dya|大雁|DYX|dayan|dy|787@dya|当阳|DYN|dangyang|dy|788@dyb|丹阳北|EXH|danyangbei|dyb|789@dyd|大英东|IAW|dayingdong|dyd|790@dyd|东淤地|DBV|dongyudi|dyd|791@dyi|大营|DYV|daying|dy|792@dyu|定远|EWH|dingyuan|dy|793@dyu|岱岳|RYV|daiyue|dy|794@dyu|大元|DYZ|dayuan|dy|795@dyz|大营镇|DJP|dayingzhen|dyz|796@dyz|大营子|DZD|dayingzi|dyz|797@dzc|大战场|DTJ|dazhanchang|dzc|798@dzd|德州东|DIP|dezhoudong|dzd|799@dzh|东至|DCH|dongzhi|dz|800@dzh|低庄|DVQ|dizhuang|dz|801@dzh|东镇|DNV|dongzhen|dz|802@dzh|道州|DFZ|daozhou|dz|803@dzh|东庄|DZV|dongzhuang|dz|804@dzh|兑镇|DWV|duizhen|dz|805@dzh|豆庄|ROP|douzhuang|dz|806@dzh|定州|DXP|dingzhou|dz|807@dzy|大竹园|DZY|dazhuyuan|dzy|808@dzz|大杖子|DAP|dazhangzi|dzz|809@dzz|豆张庄|RZP|douzhangzhuang|dzz|810@ebi|峨边|EBW|ebian|eb|811@edm|二道沟门|RDP|erdaogoumen|edgm|812@edw|二道湾|RDX|erdaowan|edw|813@ees|鄂尔多斯|EEC|eerduosi|eeds|814@elo|二龙|RLD|erlong|el|815@elt|二龙山屯|ELA|erlongshantun|elst|816@eme|峨眉|EMW|emei|em|817@emh|二密河|RML|ermihe|emh|818@epi|恩平|PXQ|enping|ep|819@eyi|二营|RYJ|erying|ey|820@ezh|鄂州|ECN|ezhou|ez|821@fan|福安|FAS|fuan|fa|822@fch|丰城|FCG|fengcheng|fc|823@fcn|丰城南|FNG|fengchengnan|fcn|824@fdo|肥东|FIH|feidong|fd|825@fer|发耳|FEM|faer|fe|826@fha|富海|FHX|fuhai|fh|827@fha|福海|FHR|fuhai|fh|828@fhc|凤凰城|FHT|fenghuangcheng|fhc|829@fhe|汾河|FEV|fenhe|fh|830@fhu|奉化|FHH|fenghua|fh|831@fji|富锦|FIB|fujin|fj|832@fjt|范家屯|FTT|fanjiatun|fjt|833@flq|福利区|FLJ|fuliqu|flq|834@flt|福利屯|FTB|fulitun|flt|835@flz|丰乐镇|FZB|fenglezhen|flz|836@fna|阜南|FNH|funan|fn|837@fni|阜宁|AKH|funing|fn|838@fni|抚宁|FNP|funing|fn|839@fqi|福清|FQS|fuqing|fq|840@fqu|福泉|VMW|fuquan|fq|841@fsc|丰水村|FSJ|fengshuicun|fsc|842@fsh|丰顺|FUQ|fengshun|fs|843@fsh|繁峙|FSV|fanshi|fs|844@fsh|抚顺|FST|fushun|fs|845@fsk|福山口|FKP|fushankou|fsk|846@fsu|扶绥|FSZ|fusui|fs|847@ftu|冯屯|FTX|fengtun|ft|848@fty|浮图峪|FYP|futuyu|fty|849@fxd|富县东|FDY|fuxiandong|fxd|850@fxi|凤县|FXY|fengxian|fx|851@fxi|富县|FEY|fuxian|fx|852@fxi|费县|FXK|feixian|fx|853@fya|凤阳|FUH|fengyang|fy|854@fya|汾阳|FAV|fenyang|fy|855@fyb|扶余北|FBT|fuyubei|fyb|856@fyi|分宜|FYG|fenyi|fy|857@fyu|富源|FYM|fuyuan|fy|858@fyu|扶余|FYT|fuyu|fy|859@fyu|富裕|FYX|fuyu|fy|860@fzb|抚州北|FBG|fuzhoubei|fzb|861@fzh|凤州|FZY|fengzhou|fz|862@fzh|丰镇|FZC|fengzhen|fz|863@fzh|范镇|VZK|fanzhen|fz|864@gan|固安|GFP|guan|ga|865@gan|广安|VJW|guangan|ga|866@gbd|高碑店|GBP|gaobeidian|gbd|867@gbz|沟帮子|GBD|goubangzi|gbz|868@gcd|甘草店|GDJ|gancaodian|gcd|869@gch|谷城|GCN|gucheng|gc|870@gch|藁城|GEP|gaocheng|gc|871@gcu|高村|GCV|gaocun|gc|872@gcz|古城镇|GZB|guchengzhen|gcz|873@gde|广德|GRH|guangde|gd|874@gdi|贵定|GTW|guiding|gd|875@gdn|贵定南|IDW|guidingnan|gdn|876@gdo|古东|GDV|gudong|gd|877@gga|贵港|GGZ|guigang|gg|878@gga|官高|GVP|guangao|gg|879@ggm|葛根庙|GGT|gegenmiao|ggm|880@ggo|干沟|GGL|gangou|gg|881@ggu|甘谷|GGJ|gangu|gg|882@ggz|高各庄|GGP|gaogezhuang|ggz|883@ghe|甘河|GAX|ganhe|gh|884@ghe|根河|GEX|genhe|gh|885@gjd|郭家店|GDT|guojiadian|gjd|886@gjz|孤家子|GKT|gujiazi|gjz|887@gla|古浪|GLJ|gulang|gl|888@gla|皋兰|GEJ|gaolan|gl|889@glf|高楼房|GFM|gaoloufang|glf|890@glh|归流河|GHT|guiliuhe|glh|891@gli|关林|GLF|guanlin|gl|892@glu|甘洛|VOW|ganluo|gl|893@glz|郭磊庄|GLP|guoleizhuang|glz|894@gmi|高密|GMK|gaomi|gm|895@gmz|公庙子|GMC|gongmiaozi|gmz|896@gnh|工农湖|GRT|gongnonghu|gnh|897@gnn|广宁寺南|GNT|guangningsinan|gnn|898@gnw|广南卫|GNM|guangnanwei|gnw|899@gpi|高平|GPF|gaoping|gp|900@gqb|甘泉北|GEY|ganquanbei|gqb|901@gqc|共青城|GAG|gongqingcheng|gqc|902@gqk|甘旗卡|GQD|ganqika|gqk|903@gqu|甘泉|GQY|ganquan|gq|904@gqz|高桥镇|GZD|gaoqiaozhen|gqz|905@gsh|灌水|GST|guanshui|gs|906@gsh|赶水|GSW|ganshui|gs|907@gsk|孤山口|GSP|gushankou|gsk|908@gso|果松|GSL|guosong|gs|909@gsz|高山子|GSD|gaoshanzi|gsz|910@gsz|嘎什甸子|GXD|gashidianzi|gsdz|911@gta|高台|GTJ|gaotai|gt|912@gta|高滩|GAY|gaotan|gt|913@gti|古田|GTS|gutian|gt|914@gti|官厅|GTP|guanting|gt|915@gtx|官厅西|KEP|guantingxi|gtx|916@gxi|贵溪|GXG|guixi|gx|917@gya|涡阳|GYH|guoyang|gy|918@gyi|巩义|GXF|gongyi|gy|919@gyi|高邑|GIP|gaoyi|gy|920@gyn|巩义南|GYF|gongyinan|gyn|921@gyn|广元南|GAW|guangyuannan|gyn|922@gyu|固原|GUJ|guyuan|gy|923@gyu|菇园|GYL|guyuan|gy|924@gyz|公营子|GYD|gongyingzi|gyz|925@gze|光泽|GZS|guangze|gz|926@gzh|古镇|GNQ|guzhen|gz|927@gzh|固镇|GEH|guzhen|gz|928@gzh|虢镇|GZY|guozhen|gz|929@gzh|瓜州|GZJ|guazhou|gz|930@gzh|高州|GSQ|gaozhou|gz|931@gzh|盖州|GXT|gaizhou|gz|932@gzj|官字井|GOT|guanzijing|gzj|933@gzs|冠豸山|GSS|guanzhaishan|gzs|934@gzx|盖州西|GAT|gaizhouxi|gzx|935@han|淮安南|AMH|huaiannan|han|936@han|海安|HIH|haian|hax|937@han|红安|HWN|hongan|ha|938@hax|红安西|VXN|honganxi|hax|939@hba|黄柏|HBL|huangbai|hb|940@hbe|海北|HEB|haibei|hb|941@hbi|鹤壁|HAF|hebi|hb|942@hcb|会昌北|XEG|huichangbei|hcb|943@hch|华城|VCQ|huacheng|hc|944@hch|河唇|HCZ|hechun|hc|945@hch|汉川|HCN|hanchuan|hc|946@hch|海城|HCT|haicheng|hc|947@hch|合川|WKW|hechuan|hc|948@hct|黑冲滩|HCJ|heichongtan|hct|949@hcu|黄村|HCP|huangcun|hc|950@hcx|海城西|HXT|haichengxi|hcx|951@hde|化德|HGC|huade|hd|952@hdo|洪洞|HDV|hongtong|hd|953@hes|霍尔果斯|HFR|huoerguosi|hegs|954@hfe|横峰|HFG|hengfeng|hf|955@hfw|韩府湾|HXJ|hanfuwan|hfw|956@hgu|汉沽|HGP|hangu|hg|957@hgy|黄瓜园|HYM|huangguayuan|hgy|958@hgz|红光镇|IGW|hongguangzhen|hgz|959@hhe|浑河|HHT|hunhe|hh|960@hhg|红花沟|VHD|honghuagou|hhg|961@hht|黄花筒|HUD|huanghuatong|hht|962@hjd|贺家店|HJJ|hejiadian|hjd|963@hji|和静|HJR|hejing|hj|964@hji|红江|HFM|hongjiang|hj|965@hji|黑井|HIM|heijing|hj|966@hji|获嘉|HJF|huojia|hj|967@hji|河津|HJV|hejin|hj|968@hji|涵江|HJS|hanjiang|hj|969@hji|华家|HJT|huajia|hj|970@hjq|杭锦后旗|HDC|hangjinhouqi|hjhq|971@hjx|河间西|HXP|hejianxi|hjx|972@hjz|花家庄|HJM|huajiazhuang|hjz|973@hkn|河口南|HKJ|hekounan|hkn|974@hko|湖口|HKG|hukou|hk|975@hko|黄口|KOH|huangkou|hk|976@hla|呼兰|HUB|hulan|hl|977@hlb|葫芦岛北|HPD|huludaobei|hldb|978@hlh|浩良河|HHB|haolianghe|hlh|979@hlh|哈拉海|HIT|halahai|hlh|980@hli|鹤立|HOB|heli|hl|981@hli|桦林|HIB|hualin|hl|982@hli|黄陵|ULY|huangling|hl|983@hli|海林|HRB|hailin|hl|984@hli|虎林|VLB|hulin|hl|985@hli|寒岭|HAT|hanling|hl|986@hlo|和龙|HLL|helong|hl|987@hlo|海龙|HIL|hailong|hl|988@hls|哈拉苏|HAX|halasu|hls|989@hlt|呼鲁斯太|VTJ|hulusitai|hlst|990@hlz|火连寨|HLT|huolianzhai|hlz|991@hme|黄梅|VEH|huangmei|hm|992@hmy|韩麻营|HYP|hanmaying|hmy|993@hnh|黄泥河|HHL|huangnihe|hnh|994@hni|海宁|HNH|haining|hn|995@hno|惠农|HMJ|huinong|hn|996@hpi|和平|VAQ|heping|hp|997@hpz|花棚子|HZM|huapengzi|hpz|998@hqi|花桥|VQH|huaqiao|hq|999@hqi|宏庆|HEY|hongqing|hq|1000@hre|怀仁|HRV|huairen|hr|1001@hro|华容|HRN|huarong|hr|1002@hsb|华山北|HDY|huashanbei|hsb|1003@hsd|黄松甸|HDL|huangsongdian|hsd|1004@hsg|和什托洛盖|VSR|heshituoluogai|hstlg|1005@hsh|红山|VSB|hongshan|hs|1006@hsh|汉寿|VSQ|hanshou|hs|1007@hsh|衡山|HSQ|hengshan|hs|1008@hsh|黑水|HOT|heishui|hs|1009@hsh|惠山|VCH|huishan|hs|1010@hsh|虎什哈|HHP|hushiha|hsh|1011@hsp|红寺堡|HSJ|hongsipu|hsp|1012@hst|虎石台|HUT|hushitai|hst|1013@hsw|海石湾|HSO|haishiwan|hsw|1014@hsx|衡山西|HEQ|hengshanxi|hsx|1015@hsx|红砂岘|VSJ|hongshaxian|hsx|1016@hta|黑台|HQB|heitai|ht|1017@hta|桓台|VTK|huantai|ht|1018@hti|和田|VTR|hetian|ht|1019@hto|会同|VTQ|huitong|ht|1020@htz|海坨子|HZT|haituozi|htz|1021@hwa|黑旺|HWK|heiwang|hw|1022@hwa|海湾|RWH|haiwan|hw|1023@hxi|红星|VXB|hongxing|hx|1024@hxi|徽县|HYY|huixian|hx|1025@hxl|红兴隆|VHB|hongxinglong|hxl|1026@hxt|换新天|VTB|huanxintian|hxt|1027@hxt|红岘台|HTJ|hongxiantai|hxt|1028@hya|红彦|VIX|hongyan|hy|1029@hya|海晏|HFO|haiyan|hy|1030@hya|合阳|HAY|heyang|hy|1031@hya|海阳|HYK|haiyang|hy|1032@hyd|衡阳东|HVQ|hengyangdong|hyd|1033@hyi|华蓥|HUW|huaying|hy|1034@hyi|汉阴|HQY|hanyin|hy|1035@hyt|黄羊滩|HGJ|huangyangtan|hyt|1036@hyu|汉源|WHW|hanyuan|hy|1037@hyu|河源|VIQ|heyuan|hy|1038@hyu|花园|HUN|huayuan|hy|1039@hyu|湟源|HNO|huangyuan|hy|1040@hyz|黄羊镇|HYJ|huangyangzhen|hyz|1041@hzh|湖州|VZH|huzhou|hz|1042@hzh|化州|HZZ|huazhou|hz|1043@hzh|黄州|VON|huangzhou|hz|1044@hzh|霍州|HZV|huozhou|hz|1045@hzx|惠州西|VXQ|huizhouxi|hzx|1046@jba|巨宝|JRT|jubao|jb|1047@jbi|靖边|JIY|jingbian|jb|1048@jbt|金宝屯|JBD|jinbaotun|jbt|1049@jcb|晋城北|JEF|jinchengbei|jcb|1050@jch|金昌|JCJ|jinchang|jc|1051@jch|鄄城|JCK|juancheng|jc|1052@jch|交城|JNV|jiaocheng|jc|1053@jch|建昌|JFD|jianchang|jc|1054@jde|峻德|JDB|junde|jd|1055@jdi|井店|JFP|jingdian|jd|1056@jdo|鸡东|JOB|jidong|jd|1057@jdu|江都|UDH|jiangdu|jd|1058@jgs|鸡冠山|JST|jiguanshan|jgs|1059@jgt|金沟屯|VGP|jingoutun|jgt|1060@jha|静海|JHP|jinghai|jh|1061@jhe|金河|JHX|jinhe|jh|1062@jhe|锦河|JHB|jinhe|jh|1063@jhe|精河|JHR|jinghe|jh|1064@jhn|精河南|JIR|jinghenan|jhn|1065@jhu|江华|JHZ|jianghua|jh|1066@jhu|建湖|AJH|jianhu|jh|1067@jjg|纪家沟|VJD|jijiagou|jjg|1068@jji|晋江|JJS|jinjiang|jj|1069@jji|锦界|JEY|jinjie|jj|1070@jji|姜家|JJB|jiangjia|jj|1071@jji|江津|JJW|jiangjin|jj|1072@jke|金坑|JKT|jinkeng|jk|1073@jli|芨岭|JLJ|jiling|jl|1074@jmc|金马村|JMM|jinmacun|jmc|1075@jmd|江门东|JWQ|jiangmendong|jmd|1076@jme|角美|JES|jiaomei|jm|1077@jna|莒南|JOK|junan|jn|1078@jna|井南|JNP|jingnan|jn|1079@jou|建瓯|JVS|jianou|jo|1080@jpe|经棚|JPC|jingpeng|jp|1081@jqi|江桥|JQX|jiangqiao|jq|1082@jsa|九三|SSX|jiusan|js|1083@jsb|金山北|EGH|jinshanbei|jsb|1084@jsh|嘉善|JSH|jiashan|js|1085@jsh|京山|JCN|jingshan|js|1086@jsh|建始|JRN|jianshi|js|1087@jsh|稷山|JVV|jishan|js|1088@jsh|吉舒|JSL|jishu|js|1089@jsh|建设|JET|jianshe|js|1090@jsh|甲山|JOP|jiashan|js|1091@jsj|建三江|JIB|jiansanjiang|jsj|1092@jsn|嘉善南|EAH|jiashannan|jsn|1093@jst|金山屯|JTB|jinshantun|jst|1094@jst|江所田|JOM|jiangsuotian|jst|1095@jta|景泰|JTJ|jingtai|jt|1096@jtn|九台南|JNL|jiutainan|jtn|1097@jwe|吉文|JWX|jiwen|jw|1098@jxi|进贤|JUG|jinxian|jx|1099@jxi|莒县|JKK|juxian|jx|1100@jxi|嘉祥|JUK|jiaxiang|jx|1101@jxi|介休|JXV|jiexiu|jx|1102@jxi|嘉兴|JXH|jiaxing|jx|1103@jxi|井陉|JJP|jingxing|jx|1104@jxn|嘉兴南|EPH|jiaxingnan|jxn|1105@jxz|夹心子|JXT|jiaxinzi|jxz|1106@jya|姜堰|UEH|jiangyan|jy|1107@jya|简阳|JYW|jianyang|jy|1108@jya|揭阳|JRQ|jieyang|jy|1109@jya|建阳|JYS|jianyang|jy|1110@jye|巨野|JYK|juye|jy|1111@jyo|江永|JYZ|jiangyong|jy|1112@jyu|缙云|JYH|jinyun|jy|1113@jyu|靖远|JYJ|jingyuan|jy|1114@jyu|江源|SZL|jiangyuan|jy|1115@jyu|济源|JYF|jiyuan|jy|1116@jyx|靖远西|JXJ|jingyuanxi|jyx|1117@jzb|胶州北|JZK|jiaozhoubei|jzb|1118@jzd|焦作东|WEF|jiaozuodong|jzd|1119@jzh|金寨|JZH|jinzhai|jz|1120@jzh|靖州|JEQ|jingzhou|jz|1121@jzh|荆州|JBN|jingzhou|jz|1122@jzh|胶州|JXK|jiaozhou|jz|1123@jzh|晋州|JXP|jinzhou|jz|1124@jzn|锦州南|JOD|jinzhounan|jzn|1125@jzu|焦作|JOF|jiaozuo|jz|1126@jzw|旧庄窝|JVP|jiuzhuangwo|jzw|1127@jzz|金杖子|JYD|jinzhangzi|jzz|1128@kan|开安|KAT|kaian|ka|1129@kch|库车|KCR|kuche|kc|1130@kch|康城|KCP|kangcheng|kc|1131@kde|库都尔|KDX|kuduer|kde|1132@kdi|宽甸|KDT|kuandian|kd|1133@kdo|克东|KOB|kedong|kd|1134@kdz|昆都仑召|KDC|kundulunzhao|kdlz|1135@kji|开江|KAW|kaijiang|kj|1136@kjj|康金井|KJB|kangjinjing|kjj|1137@klq|喀喇其|KQX|kalaqi|klq|1138@klu|开鲁|KLC|kailu|kl|1139@kly|克拉玛依|KHR|kelamayi|klmy|1140@kpn|开平南|PVQ|kaipingnan|kpn|1141@kqi|口前|KQL|kouqian|kq|1142@ksh|昆山|KSH|kunshan|ks|1143@ksh|奎山|KAB|kuishan|ks|1144@ksh|克山|KSB|keshan|ks|1145@kto|开通|KTT|kaitong|kt|1146@kxl|康熙岭|KXZ|kangxiling|kxl|1147@kya|昆阳|KAM|kunyang|ky|1148@kyh|克一河|KHX|keyihe|kyh|1149@kyx|开原西|KXT|kaiyuanxi|kyx|1150@kzh|康庄|KZP|kangzhuang|kz|1151@lbi|来宾|UBZ|laibin|lb|1152@lbi|老边|LLT|laobian|lb|1153@lbx|灵宝西|LPF|lingbaoxi|lbx|1154@lch|龙川|LUQ|longchuan|lc|1155@lch|乐昌|LCQ|lechang|lc|1156@lch|黎城|UCP|licheng|lc|1157@lch|聊城|UCK|liaocheng|lc|1158@lcu|蓝村|LCK|lancun|lc|1159@lda|两当|LDY|liangdang|ld|1160@ldo|林东|LRC|lindong|ld|1161@ldu|乐都|LDO|ledu|ld|1162@ldx|梁底下|LDP|liangdixia|ldx|1163@ldz|六道河子|LVP|liudaohezi|ldhz|1164@lfa|鲁番|LVM|lufan|lf|1165@lfa|廊坊|LJP|langfang|lf|1166@lfa|落垡|LOP|luofa|lf|1167@lfb|廊坊北|LFP|langfangbei|lfb|1168@lfu|老府|UFD|laofu|lf|1169@lga|兰岗|LNB|langang|lg|1170@lgd|龙骨甸|LGM|longgudian|lgd|1171@lgo|芦沟|LOM|lugou|lg|1172@lgo|龙沟|LGJ|longgou|lg|1173@lgu|拉古|LGB|lagu|lg|1174@lha|临海|UFH|linhai|lh|1175@lha|林海|LXX|linhai|lh|1176@lha|拉哈|LHX|laha|lh|1177@lha|凌海|JID|linghai|lh|1178@lhe|柳河|LNL|liuhe|lh|1179@lhe|六合|KLH|liuhe|lh|1180@lhu|龙华|LHP|longhua|lh|1181@lhy|滦河沿|UNP|luanheyan|lhy|1182@lhz|六合镇|LEX|liuhezhen|lhz|1183@ljd|亮甲店|LRT|liangjiadian|ljd|1184@ljd|刘家店|UDT|liujiadian|ljd|1185@ljh|刘家河|LVT|liujiahe|ljh|1186@lji|连江|LKS|lianjiang|lj|1187@lji|庐江|UJH|lujiang|lj|1188@lji|李家|LJB|lijia|lj|1189@lji|罗江|LJW|luojiang|lj|1190@lji|廉江|LJZ|lianjiang|lj|1191@lji|两家|UJT|liangjia|lj|1192@lji|龙江|LJX|longjiang|lj|1193@lji|龙嘉|UJL|longjia|lj|1194@ljk|莲江口|LHB|lianjiangkou|ljk|1195@ljl|蔺家楼|ULK|linjialou|ljl|1196@ljp|李家坪|LIJ|lijiaping|ljp|1197@lka|兰考|LKF|lankao|lk|1198@lko|林口|LKB|linkou|lk|1199@lkp|路口铺|LKQ|lukoupu|lkp|1200@lla|老莱|LAX|laolai|ll|1201@lli|拉林|LAB|lalin|ll|1202@lli|陆良|LRM|luliang|ll|1203@lli|龙里|LLW|longli|ll|1204@lli|临澧|LWQ|linli|ll|1205@lli|兰棱|LLB|lanling|ll|1206@lli|零陵|UWZ|lingling|ll|1207@llo|卢龙|UAP|lulong|ll|1208@lmd|喇嘛甸|LMX|lamadian|lmd|1209@lmd|里木店|LMB|limudian|lmd|1210@lme|洛门|LMJ|luomen|lm|1211@lna|龙南|UNG|longnan|ln|1212@lpi|梁平|UQW|liangping|lp|1213@lpi|罗平|LPM|luoping|lp|1214@lpl|落坡岭|LPP|luopoling|lpl|1215@lps|六盘山|UPJ|liupanshan|lps|1216@lps|乐平市|LPG|lepingshi|lps|1217@lqi|临清|UQK|linqing|lq|1218@lqs|龙泉寺|UQJ|longquansi|lqs|1219@lsb|乐山北|UTW|leshanbei|ls|1220@lsc|乐善村|LUM|leshancun|lsc|1221@lsd|冷水江东|UDQ|lengshuijiangdong|lsjd|1222@lsg|连山关|LGT|lianshanguan|lsg|1223@lsg|流水沟|USP|liushuigou|lsg|1224@lsh|丽水|USH|lishui|ls|1225@lsh|陵水|LIQ|lingshui|ls|1226@lsh|罗山|LRN|luoshan|ls|1227@lsh|鲁山|LAF|lushan|ls|1228@lsh|梁山|LMK|liangshan|ls|1229@lsh|灵石|LSV|lingshi|ls|1230@lsh|露水河|LUL|lushuihe|lsh|1231@lsh|庐山|LSG|lushan|ls|1232@lsp|林盛堡|LBT|linshengpu|lsp|1233@lst|柳树屯|LSD|liushutun|lst|1234@lsz|龙山镇|LAS|longshanzhen|lsz|1235@lsz|梨树镇|LSB|lishuzhen|lsz|1236@lsz|李石寨|LET|lishizhai|lsz|1237@lta|黎塘|LTZ|litang|lt|1238@lta|轮台|LAR|luntai|lt|1239@lta|芦台|LTP|lutai|lt|1240@ltb|龙塘坝|LBM|longtangba|ltb|1241@ltu|濑湍|LVZ|laituan|lt|1242@ltx|骆驼巷|LTJ|luotuoxiang|ltx|1243@lwa|李旺|VLJ|liwang|lw|1244@lwd|莱芜东|LWK|laiwudong|lwd|1245@lws|狼尾山|LRJ|langweishan|lws|1246@lwu|灵武|LNJ|lingwu|lw|1247@lwx|莱芜西|UXK|laiwuxi|lwx|1248@lxi|朗乡|LXB|langxiang|lx|1249@lxi|陇县|LXY|longxian|lx|1250@lxi|临湘|LXQ|linxiang|lx|1251@lxi|芦溪|LUG|luxi|lx|1252@lxi|莱西|LXK|laixi|lx|1253@lxi|林西|LXC|linxi|lx|1254@lxi|滦县|UXP|luanxian|lx|1255@lya|略阳|LYY|lueyang|ly|1256@lya|莱阳|LYK|laiyang|ly|1257@lya|辽阳|LYT|liaoyang|ly|1258@lyb|临沂北|UYK|linyibei|lyb|1259@lyd|凌源东|LDD|lingyuandong|lyd|1260@lyg|连云港|UIH|lianyungang|lyg|1261@lyi|临颍|LNF|linying|ly|1262@lyi|老营|LXL|laoying|ly|1263@lyo|龙游|LMH|longyou|ly|1264@lyu|罗源|LVS|luoyuan|ly|1265@lyu|林源|LYX|linyuan|ly|1266@lyu|涟源|LAQ|lianyuan|ly|1267@lyu|涞源|LYP|laiyuan|ly|1268@lyx|耒阳西|LPQ|leiyangxi|lyx|1269@lze|临泽|LEJ|linze|lz|1270@lzg|龙爪沟|LZT|longzhuagou|lzg|1271@lzh|雷州|UAQ|leizhou|lz|1272@lzh|六枝|LIW|liuzhi|lz|1273@lzh|鹿寨|LIZ|luzhai|lz|1274@lzh|来舟|LZS|laizhou|lz|1275@lzh|龙镇|LZA|longzhen|lz|1276@lzh|拉鲊|LEM|lazha|lz|1277@lzq|兰州新区|LQJ|lanzhouxinqu|lzxq|1278@mas|马鞍山|MAH|maanshan|mas|1279@mba|毛坝|MBY|maoba|mb|1280@mbg|毛坝关|MGY|maobaguan|mbg|1281@mcb|麻城北|MBN|machengbei|mcb|1282@mch|渑池|MCF|mianchi|mc|1283@mch|明城|MCL|mingcheng|mc|1284@mch|庙城|MAP|miaocheng|mc|1285@mcn|渑池南|MNF|mianchinan|mcn|1286@mcp|茅草坪|KPM|maocaoping|mcp|1287@mdh|猛洞河|MUQ|mengdonghe|mdh|1288@mds|磨刀石|MOB|modaoshi|mds|1289@mdu|弥渡|MDF|midu|md|1290@mes|帽儿山|MRB|maoershan|mes|1291@mga|明港|MGN|minggang|mg|1292@mhk|梅河口|MHL|meihekou|mhk|1293@mhu|马皇|MHZ|mahuang|mh|1294@mjg|孟家岗|MGB|mengjiagang|mjg|1295@mla|美兰|MHQ|meilan|ml|1296@mld|汨罗东|MQQ|miluodong|mld|1297@mlh|马莲河|MHB|malianhe|mlh|1298@mli|茅岭|MLZ|maoling|ml|1299@mli|庙岭|MLL|miaoling|ml|1300@mli|茂林|MLD|maolin|ml|1301@mli|穆棱|MLB|muling|ml|1302@mli|马林|MID|malin|ml|1303@mlo|马龙|MGM|malong|ml|1304@mlt|木里图|MUD|mulitu|mlt|1305@mlu|汨罗|MLQ|miluo|ml|1306@mnh|玛纳斯湖|MNR|manasihu|mnsh|1307@mni|冕宁|UGW|mianning|mn|1308@mpa|沐滂|MPQ|mupang|mp|1309@mqh|马桥河|MQB|maqiaohe|mqh|1310@mqi|闽清|MQS|minqing|mq|1311@mqu|民权|MQF|minquan|mq|1312@msh|明水河|MUT|mingshuihe|msh|1313@msh|麻山|MAB|mashan|ms|1314@msh|眉山|MSW|meishan|ms|1315@msw|漫水湾|MKW|manshuiwan|msw|1316@msz|茂舍祖|MOM|maoshezu|msz|1317@msz|米沙子|MST|mishazi|msz|1318@mta|马踏|PWQ|mata|mt|1319@mxi|美溪|MEB|meixi|mx|1320@mxi|勉县|MVY|mianxian|mx|1321@mya|麻阳|MVQ|mayang|my|1322@myb|密云北|MUP|miyunbei|myb|1323@myi|米易|MMW|miyi|my|1324@myu|麦园|MYS|maiyuan|my|1325@myu|墨玉|MUR|moyu|my|1326@mzh|庙庄|MZJ|miaozhuang|mz|1327@mzh|米脂|MEY|mizhi|mz|1328@mzh|明珠|MFQ|mingzhu|mz|1329@nan|宁安|NAB|ningan|na|1330@nan|农安|NAT|nongan|na|1331@nbs|南博山|NBK|nanboshan|nbs|1332@nch|南仇|NCK|nanqiu|nc|1333@ncs|南城司|NSP|nanchengsi|ncs|1334@ncu|宁村|NCZ|ningcun|nc|1335@nde|宁德|NES|ningde|nd|1336@ngc|南观村|NGP|nanguancun|ngc|1337@ngd|南宫东|NFP|nangongdong|ngd|1338@ngl|南关岭|NLT|nanguanling|ngl|1339@ngu|宁国|NNH|ningguo|ng|1340@nha|宁海|NHH|ninghai|nh|1341@nhb|南华北|NHS|nanhuabei|nhb|1342@nhc|南河川|NHJ|nanhechuan|nhc|1343@nhz|泥河子|NHD|nihezi|nhz|1344@nji|宁家|NVT|ningjia|nj|1345@nji|南靖|NJS|nanjing|nj|1346@nji|牛家|NJB|niujia|nj|1347@nji|能家|NJD|nengjia|nj|1348@nko|南口|NKP|nankou|nk|1349@nkq|南口前|NKT|nankouqian|nkq|1350@nla|南朗|NNQ|nanlang|nl|1351@nli|乃林|NLD|nailin|nl|1352@nlk|尼勒克|NIR|nileke|nlk|1353@nlu|那罗|ULZ|naluo|nl|1354@nlx|宁陵县|NLF|ninglingxian|nlx|1355@nma|奈曼|NMD|naiman|nm|1356@nmi|宁明|NMZ|ningming|nm|1357@nmu|南木|NMX|nanmu|nm|1358@npn|南平南|NNS|nanpingnan|npn|1359@npu|那铺|NPZ|napu|np|1360@nqi|南桥|NQD|nanqiao|nq|1361@nqu|那曲|NQO|naqu|nq|1362@nqu|暖泉|NQJ|nuanquan|nq|1363@nta|南台|NTT|nantai|nt|1364@nto|南头|NOQ|nantou|nt|1365@nwu|宁武|NWV|ningwu|nw|1366@nwz|南湾子|NWP|nanwanzi|nwz|1367@nxb|南翔北|NEH|nanxiangbei|nxb|1368@nxi|宁乡|NXQ|ningxiang|nx|1369@nxi|内乡|NXF|neixiang|nx|1370@nxt|牛心台|NXT|niuxintai|nxt|1371@nyu|南峪|NUP|nanyu|ny|1372@nzg|娘子关|NIP|niangziguan|nzg|1373@nzh|南召|NAF|nanzhao|nz|1374@nzm|南杂木|NZT|nanzamu|nzm|1375@pan|蓬安|PAW|pengan|pa|1376@pan|平安|PAL|pingan|pa|1377@pay|平安驿|PNO|pinganyi|pay|1378@paz|磐安镇|PAJ|pananzhen|paz|1379@paz|平安镇|PZT|pinganzhen|paz|1380@pcd|蒲城东|PEY|puchengdong|pcd|1381@pch|蒲城|PCY|pucheng|pc|1382@pde|裴德|PDB|peide|pd|1383@pdi|偏店|PRP|piandian|pd|1384@pdx|平顶山西|BFF|pingdingshanxi|pdsx|1385@pdx|坡底下|PXJ|podixia|pdx|1386@pet|瓢儿屯|PRT|piaoertun|pet|1387@pfa|平房|PFB|pingfang|pf|1388@pga|平岗|PGL|pinggang|pg|1389@pgu|平关|PGM|pingguan|pg|1390@pgu|盘关|PAM|panguan|pg|1391@pgu|平果|PGZ|pingguo|pg|1392@phb|徘徊北|PHP|paihuaibei|phb|1393@phk|平河口|PHM|pinghekou|phk|1394@phu|平湖|PHQ|pinghu|ph|1395@pjb|盘锦北|PBD|panjinbei|pjb|1396@pjd|潘家店|PDP|panjiadian|pjd|1397@pkn|皮口南|PKT|pikounan|pk|1398@pld|普兰店|PLT|pulandian|pld|1399@pli|偏岭|PNT|pianling|pl|1400@psh|平山|PSB|pingshan|ps|1401@psh|彭山|PSW|pengshan|ps|1402@psh|皮山|PSR|pishan|ps|1403@psh|磐石|PSL|panshi|ps|1404@psh|平社|PSV|pingshe|ps|1405@psh|彭水|PHW|pengshui|ps|1406@pta|平台|PVT|pingtai|pt|1407@pti|平田|PTM|pingtian|pt|1408@pti|莆田|PTS|putian|pt|1409@ptq|葡萄菁|PTW|putaojing|ptq|1410@pwa|普湾|PWT|puwan|pw|1411@pwa|平旺|PWV|pingwang|pw|1412@pxg|平型关|PGV|pingxingguan|pxg|1413@pxi|普雄|POW|puxiong|px|1414@pxi|郫县|PWW|pixian|px|1415@pya|平洋|PYX|pingyang|py|1416@pya|彭阳|PYJ|pengyang|py|1417@pya|平遥|PYV|pingyao|py|1418@pyi|平邑|PIK|pingyi|py|1419@pyp|平原堡|PPJ|pingyuanpu|pyp|1420@pyu|平原|PYK|pingyuan|py|1421@pyu|平峪|PYP|pingyu|py|1422@pze|彭泽|PZG|pengze|pz|1423@pzh|邳州|PJH|pizhou|pz|1424@pzh|平庄|PZD|pingzhuang|pz|1425@pzi|泡子|POD|paozi|pz|1426@pzn|平庄南|PND|pingzhuangnan|pzn|1427@qan|乾安|QOT|qianan|qa|1428@qan|庆安|QAB|qingan|qa|1429@qan|迁安|QQP|qianan|qa|1430@qdb|祁东北|QRQ|qidongbei|qd|1431@qdi|七甸|QDM|qidian|qd|1432@qfd|曲阜东|QAK|qufudong|qfd|1433@qfe|庆丰|QFT|qingfeng|qf|1434@qft|奇峰塔|QVP|qifengta|qft|1435@qfu|曲阜|QFK|qufu|qf|1436@qha|琼海|QYQ|qionghai|qh|1437@qhd|秦皇岛|QTP|qinhuangdao|qhd|1438@qhe|千河|QUY|qianhe|qh|1439@qhe|清河|QIP|qinghe|qh|1440@qhm|清河门|QHD|qinghemen|qhm|1441@qhy|清华园|QHP|qinghuayuan|qhy|1442@qji|全椒|INH|quanjiao|qj|1443@qji|渠旧|QJZ|qujiu|qj|1444@qji|潜江|QJN|qianjiang|qj|1445@qji|秦家|QJB|qinjia|qj|1446@qji|綦江|QJW|qijiang|qj|1447@qjp|祁家堡|QBT|qijiapu|qjp|1448@qjx|清涧县|QNY|qingjianxian|qjx|1449@qjz|秦家庄|QZV|qinjiazhuang|qjz|1450@qlh|七里河|QLD|qilihe|qlh|1451@qli|秦岭|QLY|qinling|ql|1452@qli|渠黎|QLZ|quli|ql|1453@qlo|青龙|QIB|qinglong|ql|1454@qls|青龙山|QGH|qinglongshan|qls|1455@qme|祁门|QIH|qimen|qm|1456@qmt|前磨头|QMP|qianmotou|qmt|1457@qsh|青山|QSB|qingshan|qs|1458@qsh|确山|QSN|queshan|qs|1459@qsh|前山|QXQ|qianshan|qs|1460@qsh|清水|QUJ|qingshui|qs|1461@qsy|戚墅堰|QYH|qishuyan|qsy|1462@qti|青田|QVH|qingtian|qt|1463@qto|桥头|QAT|qiaotou|qt|1464@qtx|青铜峡|QTJ|qingtongxia|qtx|1465@qwe|前卫|QWD|qianwei|qw|1466@qwt|前苇塘|QWP|qianweitang|qwt|1467@qxi|渠县|QRW|quxian|qx|1468@qxi|祁县|QXV|qixian|qx|1469@qxi|青县|QXP|qingxian|qx|1470@qxi|桥西|QXJ|qiaoxi|qx|1471@qxu|清徐|QUV|qingxu|qx|1472@qxy|旗下营|QXC|qixiaying|qxy|1473@qya|千阳|QOY|qianyang|qy|1474@qya|沁阳|QYF|qinyang|qy|1475@qya|泉阳|QYL|quanyang|qy|1476@qyb|祁阳北|QVQ|qiyangbei|qy|1477@qyi|七营|QYJ|qiying|qy|1478@qys|庆阳山|QSJ|qingyangshan|qys|1479@qyu|清远|QBQ|qingyuan|qy|1480@qyu|清原|QYT|qingyuan|qy|1481@qzd|钦州东|QDZ|qinzhoudong|qzd|1482@qzh|钦州|QRZ|qinzhou|qz|1483@qzs|青州市|QZK|qingzhoushi|qzs|1484@ran|瑞安|RAH|ruian|ra|1485@rch|荣昌|RCW|rongchang|rc|1486@rch|瑞昌|RCG|ruichang|rc|1487@rga|如皋|RBH|rugao|rg|1488@rgu|容桂|RUQ|ronggui|rg|1489@rqi|任丘|RQP|renqiu|rq|1490@rsh|乳山|ROK|rushan|rs|1491@rsh|融水|RSZ|rongshui|rs|1492@rsh|热水|RSD|reshui|rs|1493@rxi|容县|RXZ|rongxian|rx|1494@rya|饶阳|RVP|raoyang|ry|1495@rya|汝阳|RYF|ruyang|ry|1496@ryh|绕阳河|RHD|raoyanghe|ryh|1497@rzh|汝州|ROF|ruzhou|rz|1498@sba|石坝|OBJ|shiba|sb|1499@sbc|上板城|SBP|shangbancheng|sbc|1500@sbi|施秉|AQW|shibing|sb|1501@sbn|上板城南|OBP|shangbanchengnan|sbcn|1502@sby|世博园|ZWT|shiboyuan|sby|1503@scb|双城北|SBB|shuangchengbei|scb|1504@sch|舒城|OCH|shucheng|sc|1505@sch|商城|SWN|shangcheng|sc|1506@sch|莎车|SCR|shache|sc|1507@sch|顺昌|SCS|shunchang|sc|1508@sch|神池|SMV|shenchi|sc|1509@sch|沙城|SCP|shacheng|sc|1510@sch|石城|SCT|shicheng|sc|1511@scz|山城镇|SCL|shanchengzhen|scz|1512@sda|山丹|SDJ|shandan|sd|1513@sde|顺德|ORQ|shunde|sd|1514@sde|绥德|ODY|suide|sd|1515@sdo|水洞|SIL|shuidong|sd|1516@sdu|商都|SXC|shangdu|sd|1517@sdu|十渡|SEP|shidu|sd|1518@sdw|四道湾|OUD|sidaowan|sdw|1519@sdy|顺德学院|OJQ|shundexueyuan|sdxy|1520@sfa|绅坊|OLH|shenfang|sf|1521@sfe|双丰|OFB|shuangfeng|sf|1522@sft|四方台|STB|sifangtai|sft|1523@sfu|水富|OTW|shuifu|sf|1524@sgk|三关口|OKJ|sanguankou|sgk|1525@sgl|桑根达来|OGC|sanggendalai|sgdl|1526@sgu|韶关|SNQ|shaoguan|sg|1527@sgz|上高镇|SVK|shanggaozhen|sgz|1528@sha|上杭|JBS|shanghang|sh|1529@sha|沙海|SED|shahai|sh|1530@she|蜀河|SHY|shuhe|sh|1531@she|松河|SBM|songhe|sh|1532@she|沙河|SHP|shahe|sh|1533@shk|沙河口|SKT|shahekou|shk|1534@shl|赛汗塔拉|SHC|saihantala|shtl|1535@shs|沙河市|VOP|shaheshi|shs|1536@shs|沙后所|SSD|shahousuo|shs|1537@sht|山河屯|SHL|shanhetun|sht|1538@shx|三河县|OXP|sanhexian|shx|1539@shy|四合永|OHD|siheyong|shy|1540@shz|三汇镇|OZW|sanhuizhen|shz|1541@shz|双河镇|SEL|shuanghezhen|shz|1542@shz|石河子|SZR|shihezi|shz|1543@shz|三合庄|SVP|sanhezhuang|shz|1544@sjd|三家店|ODP|sanjiadian|sjd|1545@sjh|水家湖|SQH|shuijiahu|sjh|1546@sjh|沈家河|OJJ|shenjiahe|sjh|1547@sjh|松江河|SJL|songjianghe|sjh|1548@sji|尚家|SJB|shangjia|sj|1549@sji|孙家|SUB|sunjia|sj|1550@sji|沈家|OJB|shenjia|sj|1551@sji|双吉|SML|shuangji|sj|1552@sji|松江|SAH|songjiang|sj|1553@sjk|三江口|SKD|sanjiangkou|sjk|1554@sjl|司家岭|OLK|sijialing|sjl|1555@sjn|松江南|IMH|songjiangnan|sjn|1556@sjn|石景山南|SRP|shijingshannan|sjsn|1557@sjt|邵家堂|SJJ|shaojiatang|sjt|1558@sjx|三江县|SOZ|sanjiangxian|sjx|1559@sjz|三家寨|SMM|sanjiazhai|sjz|1560@sjz|十家子|SJD|shijiazi|sjz|1561@sjz|松江镇|OZL|songjiangzhen|sjz|1562@sjz|施家嘴|SHM|shijiazui|sjz|1563@sjz|深井子|SWT|shenjingzi|sjz|1564@sld|什里店|OMP|shilidian|sld|1565@sle|疏勒|SUR|shule|sl|1566@slh|疏勒河|SHJ|shulehe|slh|1567@slh|舍力虎|VLD|shelihu|slh|1568@sli|石磷|SPB|shilin|sl|1569@sli|石林|SLM|shilin|sl|1570@sli|双辽|ZJD|shuangliao|sl|1571@sli|绥棱|SIB|suiling|sl|1572@sli|石岭|SOL|shiling|sl|1573@sln|石林南|LNM|shilinnan|sln|1574@slo|石龙|SLQ|shilong|sl|1575@slq|萨拉齐|SLC|salaqi|slq|1576@slu|索伦|SNT|suolun|sl|1577@slu|商洛|OLY|shangluo|sl|1578@slz|沙岭子|SLP|shalingzi|slz|1579@smb|石门县北|VFQ|shimenxianbei|smxb|1580@smn|三门峡南|SCF|sanmenxianan|smxn|1581@smx|三门县|OQH|sanmenxian|smx|1582@smx|石门县|OMQ|shimenxian|smx|1583@smx|三门峡西|SXF|sanmenxiaxi|smxx|1584@sni|肃宁|SYP|suning|sn|1585@son|宋|SOB|song|son|1586@spa|双牌|SBZ|shuangpai|sp|1587@spb|沙坪坝|CYW|shapingba|spb|1588@spd|四平东|PPT|sipingdong|spd|1589@spi|遂平|SON|suiping|sp|1590@spt|沙坡头|SFJ|shapotou|spt|1591@sqi|沙桥|SQM|shaqiao|sq|1592@sqn|商丘南|SPF|shangqiunan|sqn|1593@squ|水泉|SID|shuiquan|sq|1594@sqx|石泉县|SXY|shiquanxian|sqx|1595@sqz|石桥子|SQT|shiqiaozi|sqz|1596@src|石人城|SRB|shirencheng|src|1597@sre|石人|SRL|shiren|sr|1598@ssh|山市|SQB|shanshi|ss|1599@ssh|神树|SWB|shenshu|ss|1600@ssh|鄯善|SSR|shanshan|ss|1601@ssh|三水|SJQ|sanshui|ss|1602@ssh|泗水|OSK|sishui|ss|1603@ssh|石山|SAD|shishan|ss|1604@ssh|松树|SFT|songshu|ss|1605@ssh|首山|SAT|shoushan|ss|1606@ssj|三十家|SRD|sanshijia|ssj|1607@ssp|三十里堡|SST|sanshilipu|sslp|1608@ssz|双水镇|PQQ|shuangshuizhen|ssz|1609@ssz|松树镇|SSL|songshuzhen|ssz|1610@sta|松桃|MZQ|songtao|st|1611@sth|索图罕|SHX|suotuhan|sth|1612@stj|三堂集|SDH|santangji|stj|1613@sto|石头|OTB|shitou|st|1614@sto|神头|SEV|shentou|st|1615@stu|沙沱|SFM|shatuo|st|1616@swa|上万|SWP|shangwan|sw|1617@swu|孙吴|SKB|sunwu|sw|1618@swx|沙湾县|SXR|shawanxian|swx|1619@sxi|歙县|OVH|shexian|sx|1620@sxi|遂溪|SXZ|suixi|sx|1621@sxi|沙县|SAS|shaxian|sx|1622@sxi|绍兴|SOH|shaoxing|sx|1623@sxi|石岘|SXL|shixian|sx|1624@sxp|上西铺|SXM|shangxipu|sxp|1625@sxz|石峡子|SXJ|shixiazi|sxz|1626@sya|沭阳|FMH|shuyang|sy|1627@sya|绥阳|SYB|suiyang|sy|1628@sya|寿阳|SYV|shouyang|sy|1629@sya|水洋|OYP|shuiyang|sy|1630@syc|三阳川|SYJ|sanyangchuan|syc|1631@syd|上腰墩|SPJ|shangyaodun|syd|1632@syi|三营|OEJ|sanying|sy|1633@syi|顺义|SOP|shunyi|sy|1634@syj|三义井|OYD|sanyijing|syj|1635@syp|三源浦|SYL|sanyuanpu|syp|1636@syu|上虞|BDH|shangyu|sy|1637@syu|三原|SAY|sanyuan|sy|1638@syu|上园|SUD|shangyuan|sy|1639@syu|水源|OYJ|shuiyuan|sy|1640@syz|桑园子|SAJ|sangyuanzi|syz|1641@szb|绥中北|SND|suizhongbei|szb|1642@szb|苏州北|OHH|suzhoubei|szb|1643@szd|宿州东|SRH|suzhoudong|szd|1644@szd|深圳东|BJQ|shenzhendong|szd|1645@szh|深州|OZP|shenzhou|sz|1646@szh|孙镇|OZY|sunzhen|sz|1647@szh|绥中|SZD|suizhong|sz|1648@szh|尚志|SZB|shangzhi|sz|1649@szh|师庄|SNM|shizhuang|sz|1650@szi|松滋|SIN|songzi|sz|1651@szo|师宗|SEM|shizong|sz|1652@szq|苏州园区|KAH|suzhouyuanqu|szyq|1653@szq|苏州新区|ITH|suzhouxinqu|szxq|1654@tan|泰安|TMK|taian|ta|1655@tan|台安|TID|taian|ta|1656@tay|通安驿|TAJ|tonganyi|tay|1657@tba|桐柏|TBF|tongbai|tb|1658@tbe|通北|TBB|tongbei|tb|1659@tch|桐城|TTH|tongcheng|tc|1660@tch|汤池|TCX|tangchi|tc|1661@tch|郯城|TZK|tancheng|tc|1662@tch|铁厂|TCL|tiechang|tc|1663@tcu|桃村|TCK|taocun|tc|1664@tda|通道|TRQ|tongdao|td|1665@tdo|田东|TDZ|tiandong|td|1666@tga|天岗|TGL|tiangang|tg|1667@tgl|土贵乌拉|TGC|tuguiwula|tgwl|1668@tgo|通沟|TOL|tonggou|tg|1669@tgu|太谷|TGV|taigu|tg|1670@tha|塔哈|THX|taha|th|1671@tha|棠海|THM|tanghai|th|1672@the|唐河|THF|tanghe|th|1673@the|泰和|THG|taihe|th|1674@thu|太湖|TKH|taihu|th|1675@tji|团结|TIX|tuanjie|tj|1676@tjj|谭家井|TNJ|tanjiajing|tjj|1677@tjt|陶家屯|TOT|taojiatun|tjt|1678@tjw|唐家湾|PDQ|tangjiawan|tjw|1679@tjz|统军庄|TZP|tongjunzhuang|tjz|1680@tld|吐列毛杜|TMD|tuliemaodu|tlmd|1681@tlh|图里河|TEX|tulihe|tlh|1682@tli|铜陵|TJH|tongling|tl|1683@tli|田林|TFZ|tianlin|tl|1684@tli|亭亮|TIZ|tingliang|tl|1685@tli|铁力|TLB|tieli|tl|1686@tlx|铁岭西|PXT|tielingxi|tlx|1687@tmb|图们北|QSL|tumenbei|tmb|1688@tme|天门|TMN|tianmen|tm|1689@tmn|天门南|TNN|tianmennan|tmn|1690@tms|太姥山|TLS|taimushan|tms|1691@tmt|土牧尔台|TRC|tumuertai|tmet|1692@tmz|土门子|TCJ|tumenzi|tmz|1693@tna|洮南|TVT|taonan|tn|1694@tna|潼南|TVW|tongnan|tn|1695@tpc|太平川|TIT|taipingchuan|tpc|1696@tpz|太平镇|TEB|taipingzhen|tpz|1697@tqi|图强|TQX|tuqiang|tq|1698@tqi|台前|TTK|taiqian|tq|1699@tql|天桥岭|TQL|tianqiaoling|tql|1700@tqz|土桥子|TQJ|tuqiaozi|tqz|1701@tsc|汤山城|TCT|tangshancheng|tsc|1702@tsh|桃山|TAB|taoshan|ts|1703@tsh|台山|PUQ|taishan|ts|1704@tsz|塔石嘴|TIM|tashizui|tsz|1705@ttu|通途|TUT|tongtu|tt|1706@twh|汤旺河|THB|tangwanghe|twh|1707@txi|同心|TXJ|tongxin|tx|1708@txi|土溪|TSW|tuxi|tx|1709@txi|桐乡|TCH|tongxiang|tx|1710@tya|田阳|TRZ|tianyang|ty|1711@tyi|天义|TND|tianyi|ty|1712@tyi|汤阴|TYF|tangyin|ty|1713@tyl|驼腰岭|TIL|tuoyaoling|tyl|1714@tys|太阳山|TYJ|taiyangshan|tys|1715@tyu|汤原|TYB|tangyuan|ty|1716@tyy|塔崖驿|TYP|tayayi|tyy|1717@tzd|滕州东|TEK|tengzhoudong|tzd|1718@tzh|台州|TZH|taizhou|tz|1719@tzh|天祝|TZJ|tianzhu|tz|1720@tzh|滕州|TXK|tengzhou|tz|1721@tzh|天镇|TZV|tianzhen|tz|1722@tzl|桐子林|TEW|tongzilin|tzl|1723@tzs|天柱山|QWH|tianzhushan|tzs|1724@wan|文安|WBP|wenan|wa|1725@wan|武安|WAP|wuan|wa|1726@waz|王安镇|WVP|wanganzhen|waz|1727@wbu|吴堡|WUY|wubu|wb|1728@wca|旺苍|WEW|wangcang|wc|1729@wcg|五叉沟|WCT|wuchagou|wcg|1730@wch|文昌|WEQ|wenchang|wc|1731@wch|温春|WDB|wenchun|wc|1732@wdc|五大连池|WRB|wudalianchi|wdlc|1733@wde|文登|WBK|wendeng|wd|1734@wdg|五道沟|WDL|wudaogou|wdg|1735@wdh|五道河|WHP|wudaohe|wdh|1736@wdi|文地|WNZ|wendi|wd|1737@wdo|卫东|WVT|weidong|wd|1738@wds|武当山|WRN|wudangshan|wds|1739@wdu|望都|WDP|wangdu|wd|1740@weh|乌尔旗汗|WHX|wuerqihan|weqh|1741@wfa|潍坊|WFK|weifang|wf|1742@wft|万发屯|WFB|wanfatun|wft|1743@wfu|王府|WUT|wangfu|wf|1744@wfx|瓦房店西|WXT|wafangdianxi|wfdx|1745@wga|王岗|WGB|wanggang|wg|1746@wgo|武功|WGY|wugong|wg|1747@wgo|湾沟|WGL|wangou|wg|1748@wgt|吴官田|WGM|wuguantian|wgt|1749@wha|乌海|WVC|wuhai|wh|1750@whe|苇河|WHB|weihe|wh|1751@whu|卫辉|WHF|weihui|wh|1752@wjc|吴家川|WCJ|wujiachuan|wjc|1753@wji|五家|WUB|wujia|wj|1754@wji|威箐|WAM|weiqing|wj|1755@wji|午汲|WJP|wuji|wj|1756@wji|渭津|WJL|weijin|wj|1757@wjw|王家湾|WJJ|wangjiawan|wjw|1758@wke|倭肯|WQB|woken|wk|1759@wks|五棵树|WKT|wukeshu|wks|1760@wlb|五龙背|WBT|wulongbei|wlb|1761@wld|乌兰哈达|WLC|wulanhada|wlhd|1762@wle|万乐|WEB|wanle|wl|1763@wlg|瓦拉干|WVX|walagan|wlg|1764@wli|温岭|VHH|wenling|wl|1765@wli|五莲|WLK|wulian|wl|1766@wlq|乌拉特前旗|WQC|wulateqianqi|wltqq|1767@wls|乌拉山|WSC|wulashan|wls|1768@wlt|卧里屯|WLX|wolitun|wlt|1769@wnb|渭南北|WBY|weinanbei|wnb|1770@wne|乌奴耳|WRX|wunuer|wne|1771@wni|万宁|WNQ|wanning|wn|1772@wni|万年|WWG|wannian|wn|1773@wnn|渭南南|WVY|weinannan|wnn|1774@wnz|渭南镇|WNJ|weinanzhen|wnz|1775@wpi|沃皮|WPT|wopi|wp|1776@wqi|吴桥|WUP|wuqiao|wq|1777@wqi|汪清|WQL|wangqing|wq|1778@wqi|武清|WWP|wuqing|wq|1779@wsh|武山|WSJ|wushan|ws|1780@wsh|文水|WEV|wenshui|ws|1781@wsz|魏善庄|WSP|weishanzhuang|wsz|1782@wto|王瞳|WTP|wangtong|wt|1783@wts|五台山|WSV|wutaishan|wts|1784@wtz|王团庄|WZJ|wangtuanzhuang|wtz|1785@wwu|五五|WVR|wuwu|ww|1786@wxd|无锡东|WGH|wuxidong|wxd|1787@wxi|卫星|WVB|weixing|wx|1788@wxi|闻喜|WXV|wenxi|wx|1789@wxi|武乡|WVV|wuxiang|wx|1790@wxq|无锡新区|IFH|wuxixinqu|wxxq|1791@wxu|武穴|WXN|wuxue|wx|1792@wxu|吴圩|WYZ|wuxu|wx|1793@wya|王杨|WYB|wangyang|wy|1794@wyi|武义|RYH|wuyi|wy|1795@wyi|五营|WWB|wuying|wy|1796@wyt|瓦窑田|WIM|wayaotian|wyt|1797@wyu|五原|WYC|wuyuan|wy|1798@wzg|苇子沟|WZL|weizigou|wzg|1799@wzh|韦庄|WZY|weizhuang|wz|1800@wzh|五寨|WZV|wuzhai|wz|1801@wzt|王兆屯|WZB|wangzhaotun|wzt|1802@wzz|微子镇|WQP|weizizhen|wzz|1803@wzz|魏杖子|WKD|weizhangzi|wzz|1804@xan|新安|EAM|xinan|xa|1805@xan|兴安|XAZ|xingan|xa|1806@xax|新安县|XAF|xinanxian|xax|1807@xba|新保安|XAP|xinbaoan|xba|1808@xbc|下板城|EBP|xiabancheng|xbc|1809@xbl|西八里|XLP|xibali|xbl|1810@xch|宣城|ECH|xuancheng|xc|1811@xch|兴城|XCD|xingcheng|xc|1812@xcu|小村|XEM|xiaocun|xc|1813@xcy|新绰源|XRX|xinchuoyuan|xcy|1814@xcz|下城子|XCB|xiachengzi|xcz|1815@xcz|新城子|XCT|xinchengzi|xcz|1816@xde|喜德|EDW|xide|xd|1817@xdj|小得江|EJM|xiaodejiang|xdj|1818@xdm|西大庙|XMP|xidamiao|xdm|1819@xdo|小董|XEZ|xiaodong|xd|1820@xdo|小东|XOD|xiaodong|xd|1821@xfe|信丰|EFG|xinfeng|xf|1822@xfe|襄汾|XFV|xiangfen|xf|1823@xfe|息烽|XFW|xifeng|xf|1824@xga|新干|EGG|xingan|xg|1825@xga|孝感|XGN|xiaogan|xg|1826@xgc|西固城|XUJ|xigucheng|xgc|1827@xgu|西固|XIJ|xigu|xg|1828@xgy|夏官营|XGJ|xiaguanying|xgy|1829@xgz|西岗子|NBB|xigangzi|xgz|1830@xhe|襄河|XXB|xianghe|xh|1831@xhe|新和|XIR|xinhe|xh|1832@xhe|宣和|XWJ|xuanhe|xh|1833@xhj|斜河涧|EEP|xiehejian|xhj|1834@xht|新华屯|XAX|xinhuatun|xht|1835@xhu|新华|XHB|xinhua|xh|1836@xhu|新化|EHQ|xinhua|xh|1837@xhu|宣化|XHP|xuanhua|xh|1838@xhx|兴和西|XEC|xinghexi|xhx|1839@xhy|小河沿|XYD|xiaoheyan|xhy|1840@xhy|下花园|XYP|xiahuayuan|xhy|1841@xhz|小河镇|EKY|xiaohezhen|xhz|1842@xji|徐家|XJB|xujia|xj|1843@xji|峡江|EJG|xiajiang|xj|1844@xji|新绛|XJV|xinjiang|xj|1845@xji|辛集|ENP|xinji|xj|1846@xji|新江|XJM|xinjiang|xj|1847@xjk|西街口|EKM|xijiekou|xjk|1848@xjt|许家屯|XJT|xujiatun|xjt|1849@xjt|许家台|XTJ|xujiatai|xjt|1850@xjz|谢家镇|XMT|xiejiazhen|xjz|1851@xka|兴凯|EKB|xingkai|xk|1852@xla|小榄|EAQ|xiaolan|xl|1853@xla|香兰|XNB|xianglan|xl|1854@xld|兴隆店|XDD|xinglongdian|xld|1855@xle|新乐|ELP|xinle|xl|1856@xli|新林|XPX|xinlin|xl|1857@xli|小岭|XLB|xiaoling|xl|1858@xli|新李|XLJ|xinli|xl|1859@xli|西林|XYB|xilin|xl|1860@xli|西柳|GCT|xiliu|xl|1861@xli|仙林|XPH|xianlin|xl|1862@xlt|新立屯|XLD|xinlitun|xlt|1863@xlz|兴隆镇|XZB|xinglongzhen|xlz|1864@xlz|新立镇|XGT|xinlizhen|xlz|1865@xmi|新民|XMD|xinmin|xm|1866@xms|西麻山|XMB|ximashan|xms|1867@xmt|下马塘|XAT|xiamatang|xmt|1868@xna|孝南|XNV|xiaonan|xn|1869@xnb|咸宁北|XRN|xianningbei|xnb|1870@xni|兴宁|ENQ|xingning|xn|1871@xni|咸宁|XNN|xianning|xn|1872@xpd|犀浦东|XAW|xipudong|xpd|1873@xpi|西平|XPN|xiping|xp|1874@xpi|兴平|XPY|xingping|xp|1875@xpt|新坪田|XPM|xinpingtian|xpt|1876@xpu|霞浦|XOS|xiapu|xp|1877@xpu|溆浦|EPQ|xupu|xp|1878@xpu|犀浦|XIW|xipu|xp|1879@xqi|新青|XQB|xinqing|xq|1880@xqi|新邱|XQD|xinqiu|xq|1881@xqp|兴泉堡|XQJ|xingquanbu|xqp|1882@xrq|仙人桥|XRL|xianrenqiao|xrq|1883@xsg|小寺沟|ESP|xiaosigou|xsg|1884@xsh|杏树|XSB|xingshu|xs|1885@xsh|浠水|XZN|xishui|xs|1886@xsh|下社|XSV|xiashe|xs|1887@xsh|徐水|XSP|xushui|xs|1888@xsh|夏石|XIZ|xiashi|xs|1889@xsh|小哨|XAM|xiaoshao|xs|1890@xsp|新松浦|XOB|xinsongpu|xsp|1891@xst|杏树屯|XDT|xingshutun|xst|1892@xsw|许三湾|XSJ|xusanwan|xsw|1893@xta|湘潭|XTQ|xiangtan|xt|1894@xta|邢台|XTP|xingtai|xt|1895@xtx|仙桃西|XAN|xiantaoxi|xtx|1896@xtz|下台子|EIP|xiataizi|xtz|1897@xwe|徐闻|XJQ|xuwen|xw|1898@xwp|新窝铺|EPD|xinwopu|xwp|1899@xwu|修武|XWF|xiuwu|xw|1900@xxi|新县|XSN|xinxian|xx|1901@xxi|息县|ENN|xixian|xx|1902@xxi|西乡|XQY|xixiang|xx|1903@xxi|湘乡|XXQ|xiangxiang|xx|1904@xxi|西峡|XIF|xixia|xx|1905@xxi|孝西|XOV|xiaoxi|xx|1906@xxj|小新街|XXM|xiaoxinjie|xxj|1907@xxx|新兴县|XGQ|xinxingxian|xxx|1908@xxz|西小召|XZC|xixiaozhao|xxz|1909@xxz|小西庄|XXP|xiaoxizhuang|xxz|1910@xya|向阳|XDB|xiangyang|xy|1911@xya|旬阳|XUY|xunyang|xy|1912@xyb|旬阳北|XBY|xunyangbei|xyb|1913@xyd|襄阳东|XWN|xiangyangdong|xyd|1914@xye|兴业|SNZ|xingye|xy|1915@xyg|小雨谷|XHM|xiaoyugu|xyg|1916@xyi|信宜|EEQ|xinyi|xy|1917@xyj|小月旧|XFM|xiaoyuejiu|xyj|1918@xyq|小扬气|XYX|xiaoyangqi|xyq|1919@xyu|襄垣|EIF|xiangyuan|xy|1920@xyx|夏邑县|EJH|xiayixian|xyx|1921@xyx|祥云西|EXM|xiangyunxi|xyx|1922@xyy|新友谊|EYB|xinyouyi|xyy|1923@xyz|新阳镇|XZJ|xinyangzhen|xyz|1924@xzd|徐州东|UUH|xuzhoudong|xzd|1925@xzf|新帐房|XZX|xinzhangfang|xzf|1926@xzh|悬钟|XRP|xuanzhong|xz|1927@xzh|新肇|XZT|xinzhao|xz|1928@xzh|忻州|XXV|xinzhou|xz|1929@xzi|汐子|XZD|xizi|xz|1930@xzm|西哲里木|XRD|xizhelimu|xzlm|1931@xzz|新杖子|ERP|xinzhangzi|xzz|1932@yan|姚安|YAC|yaoan|ya|1933@yan|依安|YAX|yian|ya|1934@yan|永安|YAS|yongan|ya|1935@yax|永安乡|YNB|yonganxiang|yax|1936@ybl|亚布力|YBB|yabuli|ybl|1937@ybs|元宝山|YUD|yuanbaoshan|ybs|1938@yca|羊草|YAB|yangcao|yc|1939@ycd|秧草地|YKM|yangcaodi|ycd|1940@ych|阳澄湖|AIH|yangchenghu|ych|1941@ych|迎春|YYB|yingchun|yc|1942@ych|叶城|YER|yecheng|yc|1943@ych|盐池|YKJ|yanchi|yc|1944@ych|砚川|YYY|yanchuan|yc|1945@ych|阳春|YQQ|yangchun|yc|1946@ych|宜城|YIN|yicheng|yc|1947@ych|应城|YHN|yingcheng|yc|1948@ych|禹城|YCK|yucheng|yc|1949@ych|晏城|YEK|yancheng|yc|1950@ych|阳城|YNF|yangcheng|yc|1951@ych|阳岔|YAL|yangcha|yc|1952@ych|郓城|YPK|yuncheng|yc|1953@ych|雁翅|YAP|yanchi|yc|1954@ycl|云彩岭|ACP|yuncailing|ycl|1955@ycx|虞城县|IXH|yuchengxian|ycx|1956@ycz|营城子|YCT|yingchengzi|ycz|1957@yde|英德|YDQ|yingde|yd|1958@yde|永登|YDJ|yongdeng|yd|1959@ydi|尹地|YDM|yindi|yd|1960@ydi|永定|YGS|yongding|yd|1961@ydo|阳东|WLQ|yangdong|yd|1962@yds|雁荡山|YGH|yandangshan|yds|1963@ydu|于都|YDG|yudu|yd|1964@ydu|园墩|YAJ|yuandun|yd|1965@ydx|英德西|IIQ|yingdexi|ydx|1966@yfy|永丰营|YYM|yongfengying|yfy|1967@yga|杨岗|YRB|yanggang|yg|1968@yga|阳高|YOV|yanggao|yg|1969@ygu|阳谷|YIK|yanggu|yg|1970@yha|友好|YOB|youhao|yh|1971@yha|余杭|EVH|yuhang|yh|1972@yhc|沿河城|YHP|yanhecheng|yhc|1973@yhu|岩会|AEP|yanhui|yh|1974@yjh|羊臼河|YHM|yangjiuhe|yjh|1975@yji|永嘉|URH|yongjia|yj|1976@yji|营街|YAM|yingjie|yj|1977@yji|盐津|AEW|yanjin|yj|1978@yji|阳江|WRQ|yangjiang|yj|1979@yji|余江|YHG|yujiang|yj|1980@yji|燕郊|AJP|yanjiao|yj|1981@yji|姚家|YAT|yaojia|yj|1982@yjj|岳家井|YGJ|yuejiajing|yjj|1983@yjp|一间堡|YJT|yijianpu|yjp|1984@yjs|英吉沙|YIR|yingjisha|yjs|1985@yjs|云居寺|AFP|yunjusi|yjs|1986@yjz|燕家庄|AZK|yanjiazhuang|yjz|1987@yka|永康|RFH|yongkang|yk|1988@ykd|营口东|YGT|yingkoudong|ykd|1989@yla|银浪|YJX|yinlang|yl|1990@yla|永郎|YLW|yonglang|yl|1991@ylb|宜良北|YSM|yiliangbei|ylb|1992@yld|永乐店|YDY|yongledian|yld|1993@ylh|伊拉哈|YLX|yilaha|ylh|1994@yli|伊林|YLB|yilin|yl|1995@yli|杨陵|YSY|yangling|yl|1996@yli|彝良|ALW|yiliang|yl|1997@yli|杨林|YLM|yanglin|yl|1998@ylp|余粮堡|YLD|yuliangpu|ylp|1999@ylq|杨柳青|YQP|yangliuqing|ylq|2000@ylt|月亮田|YUM|yueliangtian|ylt|2001@yma|义马|YMF|yima|ym|2002@ymb|阳明堡|YVV|yangmingbu|ymb|2003@yme|玉门|YXJ|yumen|ym|2004@yme|云梦|YMN|yunmeng|ym|2005@ymo|元谋|YMM|yuanmou|ym|2006@yms|一面山|YST|yimianshan|yms|2007@yna|沂南|YNK|yinan|yn|2008@yna|宜耐|YVM|yinai|yn|2009@ynd|伊宁东|YNR|yiningdong|ynd|2010@yps|营盘水|YZJ|yingpanshui|yps|2011@ypu|羊堡|ABM|yangpu|yp|2012@yqb|阳泉北|YPP|yangquanbei|yqb|2013@yqi|乐清|UPH|yueqing|yq|2014@yqi|焉耆|YSR|yanqi|yq|2015@yqi|源迁|AQK|yuanqian|yq|2016@yqt|姚千户屯|YQT|yaoqianhutun|yqht|2017@yqu|阳曲|YQV|yangqu|yq|2018@ysg|榆树沟|YGP|yushugou|ysg|2019@ysh|月山|YBF|yueshan|ys|2020@ysh|玉石|YSJ|yushi|ys|2021@ysh|玉舍|AUM|yushe|ys|2022@ysh|偃师|YSF|yanshi|ys|2023@ysh|沂水|YUK|yishui|ys|2024@ysh|榆社|YSV|yushe|ys|2025@ysh|颍上|YVH|yingshang|ys|2026@ysh|窑上|ASP|yaoshang|ys|2027@ysh|元氏|YSP|yuanshi|ys|2028@ysl|杨树岭|YAD|yangshuling|ysl|2029@ysp|野三坡|AIP|yesanpo|ysp|2030@yst|榆树屯|YSX|yushutun|yst|2031@yst|榆树台|YUT|yushutai|yst|2032@ysz|鹰手营子|YIP|yingshouyingzi|ysyz|2033@yta|源潭|YTQ|yuantan|yt|2034@ytp|牙屯堡|YTZ|yatunpu|ytp|2035@yts|烟筒山|YSL|yantongshan|yts|2036@ytt|烟筒屯|YUX|yantongtun|ytt|2037@yws|羊尾哨|YWM|yangweishao|yws|2038@yxi|越西|YHW|yuexi|yx|2039@yxi|攸县|YOG|youxian|yx|2040@yxi|阳西|WMQ|yangxi|yx|2041@yxi|永修|ACG|yongxiu|yx|2042@yxx|玉溪西|YXM|yuxixi|yxx|2043@yya|弋阳|YIG|yiyang|yy|2044@yya|余姚|YYH|yuyao|yy|2045@yya|酉阳|AFW|youyang|yy|2046@yyd|岳阳东|YIQ|yueyangdong|yyd|2047@yyi|阳邑|ARP|yangyi|yy|2048@yyu|鸭园|YYL|yayuan|yy|2049@yyz|鸳鸯镇|YYJ|yuanyangzhen|yyz|2050@yzb|燕子砭|YZY|yanzibian|yzb|2051@yzh|仪征|UZH|yizheng|yz|2052@yzh|宜州|YSZ|yizhou|yz|2053@yzh|兖州|YZK|yanzhou|yz|2054@yzi|迤资|YQM|yizi|yz|2055@yzw|羊者窝|AEM|yangzhewo|yzw|2056@yzz|杨杖子|YZD|yangzhangzi|yzz|2057@zan|镇安|ZEY|zhenan|za|2058@zan|治安|ZAD|zhian|za|2059@zba|招柏|ZBP|zhaobai|zb|2060@zbw|张百湾|ZUP|zhangbaiwan|zbw|2061@zcc|中川机场|ZJJ|zhongchuanjichang|zcjc|2062@zch|枝城|ZCN|zhicheng|zc|2063@zch|子长|ZHY|zichang|zc|2064@zch|诸城|ZQK|zhucheng|zc|2065@zch|邹城|ZIK|zoucheng|zc|2066@zch|赵城|ZCV|zhaocheng|zc|2067@zda|章党|ZHT|zhangdang|zd|2068@zdi|正定|ZDP|zhengding|zd|2069@zdo|肇东|ZDB|zhaodong|zd|2070@zfp|照福铺|ZFM|zhaofupu|zfp|2071@zgt|章古台|ZGD|zhanggutai|zgt|2072@zgu|赵光|ZGB|zhaoguang|zg|2073@zhe|中和|ZHX|zhonghe|zh|2074@zhm|中华门|VNH|zhonghuamen|zhm|2075@zjb|枝江北|ZIN|zhijiangbei|zjb|2076@zjc|钟家村|ZJY|zhongjiacun|zjc|2077@zjg|朱家沟|ZUB|zhujiagou|zjg|2078@zjg|紫荆关|ZYP|zijingguan|zjg|2079@zji|周家|ZOB|zhoujia|zj|2080@zji|诸暨|ZDH|zhuji|zj|2081@zjn|镇江南|ZEH|zhenjiangnan|zjn|2082@zjt|周家屯|ZOD|zhoujiatun|zjt|2083@zjw|褚家湾|CWJ|zhujiawan|zjw|2084@zjx|湛江西|ZWQ|zhanjiangxi|zjx|2085@zjy|朱家窑|ZUJ|zhujiayao|zjy|2086@zjz|曾家坪子|ZBW|zengjiapingzi|zjpz|2087@zla|张兰|ZLV|zhanglan|zl|2088@zla|镇赉|ZLT|zhenlai|zl|2089@zli|枣林|ZIV|zaolin|zl|2090@zlt|扎鲁特|ZLD|zhalute|zlt|2091@zlx|扎赉诺尔西|ZXX|zhalainuoerxi|zlrex|2092@zmt|樟木头|ZOQ|zhangmutou|zmt|2093@zmu|中牟|ZGF|zhongmu|zm|2094@znd|中宁东|ZDJ|zhongningdong|znd|2095@zni|中宁|VNJ|zhongning|zn|2096@znn|中宁南|ZNJ|zhongningnan|znn|2097@zpi|镇平|ZPF|zhenping|zp|2098@zpi|漳平|ZPS|zhangping|zp|2099@zpu|泽普|ZPR|zepu|zp|2100@zqi|枣强|ZVP|zaoqiang|zq|2101@zqi|张桥|ZQY|zhangqiao|zq|2102@zqi|章丘|ZTK|zhangqiu|zq|2103@zrh|朱日和|ZRC|zhurihe|zrh|2104@zrl|泽润里|ZLM|zerunli|zrl|2105@zsb|中山北|ZGQ|zhongshanbei|zsb|2106@zsd|樟树东|ZOG|zhangshudong|zsd|2107@zsh|珠斯花|ZHD|zhusihua|zsh|2108@zsh|中山|ZSQ|zhongshan|zs|2109@zsh|柞水|ZSY|zhashui|zs|2110@zsh|钟山|ZSZ|zhongshan|zs|2111@zsh|樟树|ZSG|zhangshu|zs|2112@zwo|珠窝|ZOP|zhuwo|zw|2113@zwt|张维屯|ZWB|zhangweitun|zwt|2114@zwu|彰武|ZWD|zhangwu|zw|2115@zxi|棕溪|ZOY|zongxi|zx|2116@zxi|钟祥|ZTN|zhongxiang|zx|2117@zxi|资溪|ZXS|zixi|zx|2118@zxi|镇西|ZVT|zhenxi|zx|2119@zxi|张辛|ZIP|zhangxin|zx|2120@zxq|正镶白旗|ZXC|zhengxiangbaiqi|zxbq|2121@zya|紫阳|ZVY|ziyang|zy|2122@zya|枣阳|ZYN|zaoyang|zy|2123@zyb|竹园坝|ZAW|zhuyuanba|zyb|2124@zye|张掖|ZYJ|zhangye|zy|2125@zyu|镇远|ZUW|zhenyuan|zy|2126@zzd|漳州东|GOS|zhangzhoudong|zzd|2127@zzh|漳州|ZUS|zhangzhou|zz|2128@zzh|壮志|ZUX|zhuangzhi|zz|2129@zzh|子洲|ZZY|zizhou|zz|2130@zzh|中寨|ZZM|zhongzhai|zz|2131@zzh|涿州|ZXP|zhuozhou|zz|2132@zzi|咋子|ZAL|zhazi|zz|2133@zzs|卓资山|ZZC|zhuozishan|zzs|2134@zzx|株洲西|ZAQ|zhuzhouxi|zzx|2135@zzx|郑州西|XPF|zhengzhouxi|zzx|2136@abq|阿巴嘎旗|AQC|abagaqi|abgq|2137@aeb|阿尔山北|ARX|aershanbei|aesb|2138@alt|阿勒泰|AUR|aletai|alt|2139@are|安仁|ARG|anren|ar|2140@asx|安顺西|ASE|anshunxi|asx|2141@atx|安图西|AXL|antuxi|atx|2142@ayd|安阳东|ADF|anyangdong|ayd|2143@bba|博白|BBZ|bobai|bb|2144@bbu|八步|BBE|babu|bb|2145@bch|栟茶|FWH|bencha|bc|2146@bdd|保定东|BMP|baodingdong|bdd|2147@bfs|八方山|FGQ|bafangshan|bfs|2148@bgo|白沟|FEP|baigou|bg|2149@bha|滨海|FHP|binhai|bh|2150@bhb|滨海北|FCP|binhaibei|bhb|2151@bjn|宝鸡南|BBY|baojinan|bjn|2152@bjz|北井子|BRT|beijingzi|bjz|2153@bmj|白马井|BFQ|baimajing|bmj|2154@bqi|宝清|BUB|baoqing|bq|2155@bsh|璧山|FZW|bishan|bs|2156@bsp|白沙铺|BSN|baishapu|bsp|2157@bsx|白水县|BGY|baishuixian|bsx|2158@bta|板塘|NGQ|bantang|bt|2159@bwd|白文东|BCV|baiwendong|bwd|2160@bxc|本溪新城|BVT|benxixincheng|bxxc|2161@bxi|彬县|BXY|binxian|bx|2162@bya|宾阳|UKZ|binyang|by|2163@byd|白洋淀|FWP|baiyangdian|byd|2164@byi|百宜|FHW|baiyi|by|2165@byn|白音华南|FNC|baiyinhuanan|byhn|2166@bzd|巴中东|BDE|bazhongdong|bzd|2167@bzh|滨州|BIK|binzhou|bz|2168@bzx|霸州西|FOP|bazhouxi|bzx|2169@cch|澄城|CUY|chengcheng|cc|2170@cgb|城固北|CBY|chenggubei|cgb|2171@cgh|查干湖|VAT|chaganhu|cgh|2172@chd|巢湖东|GUH|chaohudong|chd|2173@cji|从江|KNW|congjiang|cj|2174@cjy|蔡家崖|EBV|caijiaya|cjy|2175@cka|茶卡|CVO|chaka|ck|2176@clh|长临河|FVH|changlinhe|clh|2177@cln|茶陵南|CNG|chalingnan|cln|2178@cpd|常平东|FQQ|changpingdong|cpd|2179@cpn|常平南|FPQ|changpingnan|cpn|2180@cqq|长庆桥|CQJ|changqingqiao|cqq|2181@csb|长寿北|COW|changshoubei|csb|2182@csh|长寿湖|CSE|changshouhu|csh|2183@csh|常山|CSU|changshan|cs|2184@csh|潮汕|CBQ|chaoshan|cs|2185@csx|长沙西|RXQ|changshaxi|csx|2186@cti|朝天|CTE|chaotian|ct|2187@ctn|长汀南|CNS|changtingnan|ctn|2188@cwu|长武|CWY|changwu|cw|2189@cxi|长兴|CBH|changxing|cx|2190@cxi|苍溪|CXE|cangxi|cx|2191@cxi|楚雄|CUM|chuxiong|cx|2192@cya|长阳|CYN|changyang|cy|2193@cya|潮阳|CNQ|chaoyang|cy|2194@czt|城子坦|CWT|chengzitan|czt|2195@dad|东安东|DCZ|dongandong|dad|2196@dba|德保|RBZ|debao|db|2197@dch|都昌|DCG|duchang|dc|2198@dch|东岔|DCJ|dongcha|dc|2199@dcn|东城南|IYQ|dongchengnan|dcn|2200@ddh|东戴河|RDD|dongdaihe|ddh|2201@ddx|丹东西|RWT|dandongxi|ddx|2202@deh|东二道河|DRB|dongerdaohe|dedh|2203@dfe|大丰|KRQ|dafeng|df|2204@dfn|大方南|DNE|dafangnan|dfn|2205@dgb|东港北|RGT|donggangbei|dgb|2206@dgs|大孤山|RMT|dagushan|dgs|2207@dgu|东莞|RTQ|dongguan|dg|2208@dhd|鼎湖东|UWQ|dinghudong|dhd|2209@dhs|鼎湖山|NVQ|dinghushan|dhs|2210@dji|道滘|RRQ|daojiao|dj|2211@dji|洞井|FWQ|dongjing|dj|2212@dji|垫江|DJE|dianjiang|dj|2213@dju|大苴|DIM|daju|dj|2214@dli|大荔|DNY|dali|dl|2215@dlz|大朗镇|KOQ|dalangzhen|dlz|2216@dqg|大青沟|DSD|daqinggou|dqg|2217@dqi|德清|DRH|deqing|dq|2218@dsd|东胜东|RSC|dongshengdong|dsd|2219@dsn|大石头南|DAL|dashitounan|dstn|2220@dsn|砀山南|PRH|dangshannan|dsn|2221@dtd|当涂东|OWH|dangtudong|dtd|2222@dtx|大通西|DTO|datongxi|dtx|2223@dwa|大旺|WWQ|dawang|dw|2224@dxb|定西北|DNJ|dingxibei|dxb|2225@dxd|德兴东|DDG|dexingdong|dxd|2226@dxi|德兴|DWG|dexing|dx|2227@dxs|丹霞山|IRQ|danxiashan|dxs|2228@dyb|大冶北|DBN|dayebei|dyb|2229@dyd|都匀东|KJW|duyundong|dyd|2230@dyn|东营南|DOK|dongyingnan|dyn|2231@dyu|大余|DYG|dayu|dy|2232@dzd|定州东|DOP|dingzhoudong|dzd|2233@dzh|端州|WZQ|duanzhou|dz|2234@dzn|大足南|FQW|dazunan|dzn|2235@ems|峨眉山|IXW|emeishan|ems|2236@epg|阿房宫|EGY|epanggong|epg|2237@ezd|鄂州东|EFN|ezhoudong|ezd|2238@fcb|防城港北|FBZ|fangchenggangbei|fcgb|2239@fcd|凤城东|FDT|fengchengdong|fcd|2240@fch|富川|FDZ|fuchuan|fc|2241@fcx|繁昌西|PUH|fanchangxi|fcx|2242@fdu|丰都|FUW|fengdu|fd|2243@flb|涪陵北|FEW|fulingbei|flb|2244@fli|枫林|FLN|fenglin|fl|2245@fni|富宁|FNM|funing|fn|2246@fpi|佛坪|FUY|foping|fp|2247@fqi|法启|FQE|faqi|fq|2248@frn|芙蓉南|KCQ|furongnan|frn|2249@fsh|复盛|FAW|fusheng|fs|2250@fso|抚松|FSL|fusong|fs|2251@fsx|佛山西|FOQ|foshanxi|fsx|2252@fsz|福山镇|FZQ|fushanzhen|fsz|2253@fti|福田|NZQ|futian|ft|2254@fyb|富源北|FBM|fuyuanbei|fyb|2255@fyu|抚远|FYB|fuyuan|fy|2256@fzd|抚州东|FDG|fuzhoudong|fzd|2257@fzh|抚州|FZG|fuzhou|fz|2258@gan|高安|GCG|gaoan|ga|2259@gan|广安南|VUW|guangannan|gan|2260@gan|贵安|GAE|guian|ga|2261@gbd|高碑店东|GMP|gaobeidiandong|gbdd|2262@gch|恭城|GCZ|gongcheng|gc|2263@gcn|藁城南|GUP|gaochengnan|gcn|2264@gdb|贵定北|FMW|guidingbei|gdb|2265@gdn|葛店南|GNN|gediannan|gdn|2266@gdx|贵定县|KIW|guidingxian|gdx|2267@ghb|广汉北|GVW|guanghanbei|ghb|2268@ghu|高花|HGD|gaohua|gh|2269@gju|革居|GEM|geju|gj|2270@gli|关岭|GLE|guanling|gl|2271@glx|桂林西|GEZ|guilinxi|glx|2272@gmc|光明城|IMQ|guangmingcheng|gmc|2273@gni|广宁|FBQ|guangning|gn|2274@gns|广宁寺|GQT|guangningsi|gns|2275@gnx|广南县|GXM|guangnanxian|gnx|2276@gpi|桂平|GAZ|guiping|gp|2277@gpz|弓棚子|GPT|gongpengzi|gpz|2278@gsd|赶水东|GDE|ganshuidong|gsd|2279@gsh|光山|GUN|guangshan|gs|2280@gsh|谷山|FFQ|gushan|gs|2281@gsl|观沙岭|FKQ|guanshaling|gsl|2282@gtb|古田北|GBS|gutianbei|gtb|2283@gtb|广通北|GPM|guangtongbei|gtb|2284@gtn|高台南|GAJ|gaotainan|gtn|2285@gtz|古田会址|STS|gutianhuizhi|gthz|2286@gyb|贵阳北|KQW|guiyangbei|gyb|2287@gyd|贵阳东|KEW|guiyangdong|gyd|2288@gyx|高邑西|GNP|gaoyixi|gyx|2289@han|惠安|HNS|huian|ha|2290@hbb|淮北北|PLH|huaibeibei|hbb|2291@hbd|鹤壁东|HFF|hebidong|hbd|2292@hcg|寒葱沟|HKB|hanconggou|hcg|2293@hch|霍城|SER|huocheng|hc|2294@hch|珲春|HUL|hunchun|hc|2295@hdd|邯郸东|HPP|handandong|hdd|2296@hdo|惠东|KDQ|huidong|hd|2297@hdp|哈达铺|HDJ|hadapu|hdp|2298@hdx|洪洞西|HTV|hongtongxi|hdx|2299@hdx|海东西|HDO|haidongxi|hdx|2300@heb|哈尔滨北|HTB|haerbinbei|hebb|2301@hfc|合肥北城|COH|hefeibeicheng|hfbc|2302@hfn|合肥南|ENH|hefeinan|hfn|2303@hga|黄冈|KGN|huanggang|hg|2304@hgd|黄冈东|KAN|huanggangdong|hgd|2305@hgd|横沟桥东|HNN|henggouqiaodong|hgqd|2306@hgx|黄冈西|KXN|huanggangxi|hgx|2307@hhe|洪河|HPB|honghe|hh|2308@hhn|怀化南|KAQ|huaihuanan|hhn|2309@hhq|黄河景区|HCF|huanghejingqu|hhjq|2310@hhu|花湖|KHN|huahu|hh|2311@hhu|惠环|KHQ|huihuan|hh|2312@hhu|后湖|IHN|houhu|hh|2313@hji|怀集|FAQ|huaiji|hj|2314@hkb|河口北|HBM|hekoubei|hkb|2315@hli|黄流|KLQ|huangliu|hl|2316@hln|黄陵南|VLY|huanglingnan|hln|2317@hme|鲘门|KMQ|houmen|hm|2318@hme|虎门|IUQ|humen|hm|2319@hmx|侯马西|HPV|houmaxi|hmx|2320@hna|衡南|HNG|hengnan|hn|2321@hnd|淮南东|HOH|huainandong|hnd|2322@hpu|合浦|HVZ|hepu|hp|2323@hqi|霍邱|FBH|huoqiu|hq|2324@hrd|怀仁东|HFV|huairendong|hrd|2325@hrd|华容东|HPN|huarongdong|hrd|2326@hrn|华容南|KRN|huarongnan|hrn|2327@hsb|黄石北|KSN|huangshibei|hsb|2328@hsb|黄山北|NYH|huangshanbei|hsb|2329@hsb|衡水北|IHP|hengshuibei|hsb|2330@hsd|贺胜桥东|HLN|heshengqiaodong|hsqd|2331@hsh|和硕|VUR|heshuo|hs|2332@hsn|花山南|KNN|huashannan|hsn|2333@hta|荷塘|KXQ|hetang|ht|2334@htd|黄土店|HKP|huangtudian|htd|2335@hyb|合阳北|HTY|heyangbei|hyb|2336@hyb|海阳北|HEK|haiyangbei|hyb|2337@hyi|槐荫|IYN|huaiyin|hy|2338@hyi|鄠邑|KXY|huyi|hyi|2339@hyk|花园口|HYT|huayuankou|hyk|2340@hzd|霍州东|HWV|huozhoudong|hzd|2341@hzn|惠州南|KNQ|huizhounan|hzn|2342@jan|建安|JUL|jianan|ja|2343@jch|泾川|JAJ|jingchuan|jc|2344@jdb|景德镇北|JDG|jingdezhenbei|jdzb|2345@jde|旌德|NSH|jingde|jd|2346@jfe|尖峰|PFQ|jianfeng|jf|2347@jha|近海|JHD|jinhai|jh|2348@jhx|蛟河西|JOL|jiaohexi|jhx|2349@jlb|军粮城北|JMP|junliangchengbei|jlcb|2350@jle|将乐|JLS|jiangle|jl|2351@jlh|贾鲁河|JLF|jialuhe|jlh|2352@jls|九郎山|KJQ|jiulangshan|jls|2353@jmb|即墨北|JVK|jimobei|jmb|2354@jmg|剑门关|JME|jianmenguan|jmg|2355@jnb|建宁县北|JCS|jianningxianbei|jnxb|2356@jni|江宁|JJH|jiangning|jn|2357@jnx|江宁西|OKH|jiangningxi|jnx|2358@jox|建瓯西|JUS|jianouxi|jox|2359@jqn|酒泉南|JNJ|jiuquannan|jqn|2360@jrx|句容西|JWH|jurongxi|jrx|2361@jsh|建水|JSM|jianshui|js|2362@jsh|尖山|JPQ|jianshan|js|2363@jss|界首市|JUN|jieshoushi|jss|2364@jxb|绩溪北|NRH|jixibei|jxb|2365@jxd|介休东|JDV|jiexiudong|jxd|2366@jxi|泾县|LOH|jingxian|jx|2367@jxi|靖西|JMZ|jingxi|jx|2368@jxn|进贤南|JXG|jinxiannan|jxn|2369@jyb|江油北|JBE|jiangyoubei|jyb|2370@jyn|简阳南|JOW|jianyangnan|jyn|2371@jyn|嘉峪关南|JBJ|jiayuguannan|jygn|2372@jyt|金银潭|JTN|jinyintan|jyt|2373@jyu|靖宇|JYL|jingyu|jy|2374@jyw|金月湾|PYQ|jinyuewan|jyw|2375@jyx|缙云西|PYH|jinyunxi|jyx|2376@jzh|晋中|JZV|jinzhong|jz|2377@jzh|景州|JEP|jingzhou|jz|2378@kfb|开封北|KBF|kaifengbei|kfb|2379@kfs|开福寺|FLQ|kaifusi|kfs|2380@khu|开化|KHU|kaihua|kh|2381@kln|凯里南|QKW|kailinan|kln|2382@klu|库伦|KLD|kulun|kl|2383@kmn|昆明南|KOM|kunmingnan|kmn|2384@kta|葵潭|KTQ|kuitan|kt|2385@kya|开阳|KVW|kaiyang|ky|2386@lad|隆安东|IDZ|longandong|lad|2387@lbb|来宾北|UCZ|laibinbei|lbb|2388@lbi|灵璧|GMH|lingbi|lb|2389@lbu|寮步|LTQ|liaobu|lb|2390@lby|绿博园|LCF|lvboyuan|lby|2391@lcb|隆昌北|NWW|longchangbei|lcb|2392@lcd|乐昌东|ILQ|lechangdong|lcd|2393@lch|临城|UUP|lincheng|lc|2394@lch|罗城|VCZ|luocheng|lc|2395@lch|陵城|LGK|lingcheng|lc|2396@lcz|老城镇|ACQ|laochengzhen|lcz|2397@ldb|龙洞堡|FVW|longdongbao|ldb|2398@ldn|乐都南|LVO|ledunan|ldn|2399@ldn|娄底南|UOQ|loudinan|ldn|2400@ldo|乐东|UQQ|ledong|ld|2401@ldy|离堆公园|INW|liduigongyuan|ldgy|2402@lfa|娄烦|USV|loufan|lf|2403@lfe|陆丰|LLQ|lufeng|lf|2404@lfe|龙丰|KFQ|longfeng|lf|2405@lfn|禄丰南|LQM|lufengnan|lfn|2406@lfx|临汾西|LXV|linfenxi|lfx|2407@lgn|临高南|KGQ|lingaonan|lgn|2408@lgu|麓谷|BNQ|lugu|lg|2409@lhe|滦河|UDP|luanhe|lh|2410@lhn|珞璜南|LNE|luohuangnan|lhn|2411@lhx|漯河西|LBN|luohexi|lhx|2412@ljd|罗江东|IKW|luojiangdong|ljd|2413@lji|柳江|UQZ|liujiang|lj|2414@ljn|利津南|LNK|lijinnan|ljn|2415@lkn|兰考南|LUF|lankaonan|lkn|2416@lks|龙口市|UKK|longkoushi|lks|2417@llb|兰陵北|COK|lanlingbei|llb|2418@llb|龙里北|KFW|longlibei|llb|2419@llb|沥林北|KBQ|lilinbei|llb|2420@lld|醴陵东|UKQ|lilingdong|lld|2421@lna|陇南|INJ|longnan|ln|2422@lpn|梁平南|LPE|liangpingnan|lpn|2423@lqu|礼泉|LGY|liquan|lq|2424@lsd|灵石东|UDV|lingshidong|lsd|2425@lsh|乐山|IVW|leshan|ls|2426@lsh|龙市|LAG|longshi|ls|2427@lsh|溧水|LDH|lishui|ls|2428@lsn|娄山关南|LSE|loushanguannan|lsgn|2429@lwj|洛湾三江|KRW|luowansanjiang|lwsj|2430@lxb|莱西北|LBK|laixibei|lxb|2431@lxi|岚县|UXV|lanxian|lx|2432@lya|溧阳|LEH|liyang|ly|2433@lyi|临邑|LUK|linyi|ly|2434@lyn|柳园南|LNR|liuyuannan|lyn|2435@lzb|鹿寨北|LSZ|luzhaibei|lzb|2436@lzh|阆中|LZE|langzhong|lz|2437@lzn|临泽南|LDJ|linzenan|lzn|2438@mad|马鞍山东|OMH|maanshandong|masd|2439@mch|毛陈|MHN|maochen|mc|2440@mgd|明港东|MDN|minggangdong|mgd|2441@mhn|民和南|MNO|minhenan|mhn|2442@mji|闵集|MJN|minji|mj|2443@mla|马兰|MLR|malan|ml|2444@mle|民乐|MBJ|minle|ml|2445@mle|弥勒|MLM|mile|ml|2446@mns|玛纳斯|MSR|manasi|mns|2447@mpi|牟平|MBK|muping|mp|2448@mqb|闽清北|MBS|minqingbei|mqb|2449@mqb|民权北|MIF|minquanbei|mqb|2450@msd|眉山东|IUW|meishandong|msd|2451@msh|庙山|MSN|miaoshan|ms|2452@mxi|岷县|MXJ|minxian|mx|2453@myu|门源|MYO|menyuan|my|2454@myu|暮云|KIQ|muyun|my|2455@mzb|蒙自北|MBM|mengzibei|mzb|2456@mzh|孟庄|MZF|mengzhuang|mz|2457@mzi|蒙自|MZM|mengzi|mz|2458@nbu|南部|NBE|nanbu|nb|2459@nca|南曹|NEF|nancao|nc|2460@ncb|南充北|NCE|nanchongbei|ncb|2461@nch|南城|NDG|nancheng|nc|2462@nch|南 昌|NOG|nanchang|nc|2463@ncx|南昌西|NXG|nanchangxi|ncx|2464@ndn|宁东南|NDJ|ningdongnan|ndn|2465@ndo|宁东|NOJ|ningdong|nd|2466@nfb|南芬北|NUT|nanfenbei|nfb|2467@nfe|南丰|NFG|nanfeng|nf|2468@nhd|南湖东|NDN|nanhudong|nhd|2469@nhu|南华|NAM|nanhua|nh|2470@njb|内江北|NKW|neijiangbei|njb|2471@nji|南江|FIW|nanjiang|nj|2472@njk|南江口|NDQ|nanjiangkou|njk|2473@nli|南陵|LLH|nanling|nl|2474@nmu|尼木|NMO|nimu|nm|2475@nnd|南宁东|NFZ|nanningdong|nnd|2476@nnx|南宁西|NXZ|nanningxi|nnx|2477@npb|南平北|NBS|nanpingbei|npb|2478@nqn|宁强南|NOY|ningqiangnan|nqn|2479@nxi|南雄|NCQ|nanxiong|nx|2480@nyo|纳雍|NYE|nayong|ny|2481@nyz|南阳寨|NYF|nanyangzhai|nyz|2482@pan|普安|PAN|puan|pa|2483@pax|普安县|PUE|puanxian|pax|2484@pbi|屏边|PBM|pingbian|pb|2485@pbn|平坝南|PBE|pingbanan|pbn|2486@pch|平昌|PCE|pingchang|pc|2487@pdi|普定|PGW|puding|pd|2488@pdu|平度|PAK|pingdu|pd|2489@pko|皮口|PUT|pikou|pk|2490@plc|盘龙城|PNN|panlongcheng|plc|2491@pls|蓬莱市|POK|penglaishi|pls|2492@pni|普宁|PEQ|puning|pn|2493@pnn|平南南|PAZ|pingnannan|pnn|2494@psb|彭山北|PPW|pengshanbei|psb|2495@psh|盘山|PUD|panshan|ps|2496@psh|坪上|PSK|pingshang|ps|2497@pxb|萍乡北|PBG|pingxiangbei|pxb|2498@pya|鄱阳|PYG|poyang|py|2499@pya|濮阳|PYF|puyang|py|2500@pyc|平遥古城|PDV|pingyaogucheng|pygc|2501@pyd|平原东|PUK|pingyuandong|pyd|2502@pzh|普者黑|PZM|puzhehei|pzh|2503@pzh|盘州|PAE|panzhou|pz|2504@pzh|彭州|PMW|pengzhou|pz|2505@qan|秦安|QGJ|qinan|qa|2506@qbd|青白江东|QFW|qingbaijiangdong|qbjd|2507@qch|青川|QCE|qingchuan|qc|2508@qdb|青岛北|QHK|qingdaobei|qdb|2509@qdo|祁东|QMQ|qidong|qd|2510@qdu|青堆|QET|qingdui|qd|2511@qfe|前锋|QFB|qianfeng|qf|2512@qjb|曲靖北|QBM|qujingbei|qjb|2513@qjd|綦江东|QDE|qijiangdong|qjd|2514@qji|曲江|QIM|qujiang|qj|2515@qli|青莲|QEW|qinglian|ql|2516@qqn|齐齐哈尔南|QNB|qiqihaernan|qqhen|2517@qsb|清水北|QEJ|qingshuibei|qsb|2518@qsh|青神|QVW|qingshen|qs|2519@qsh|岐山|QAY|qishan|qs|2520@qsh|庆盛|QSQ|qingsheng|qs|2521@qsx|清水县|QIJ|qingshuixian|qsx|2522@qsx|曲水县|QSO|qushuixian|qsx|2523@qxd|祁县东|QGV|qixiandong|qxd|2524@qxi|乾县|QBY|qianxian|qx|2525@qxn|旗下营南|QNC|qixiayingnan|qxyn|2526@qya|祁阳|QWQ|qiyang|qy|2527@qzn|全州南|QNZ|quanzhounan|qzn|2528@qzw|棋子湾|QZQ|qiziwan|qzw|2529@rbu|仁布|RUO|renbu|rb|2530@rcb|荣昌北|RQW|rongchangbei|rcb|2531@rch|荣成|RCK|rongcheng|rc|2532@rcx|瑞昌西|RXG|ruichangxi|rcx|2533@rdo|如东|RIH|rudong|rd|2534@rji|榕江|RVW|rongjiang|rj|2535@rkz|日喀则|RKO|rikaze|rkz|2536@rpi|饶平|RVQ|raoping|rp|2537@scl|宋城路|SFF|songchenglu|scl|2538@sdh|三道湖|SDL|sandaohu|sdh|2539@sdo|邵东|FIQ|shaodong|sd|2540@sdx|三都县|KKW|sanduxian|sdx|2541@sfa|胜芳|SUP|shengfang|sf|2542@sfb|双峰北|NFQ|shuangfengbei|sfb|2543@she|商河|SOK|shanghe|sh|2544@sho|泗洪|GQH|sihong|sh|2545@shu|四会|AHQ|sihui|sh|2546@sjd|石家庄东|SXP|shijiazhuangdong|sjzd|2547@sjn|三江南|SWZ|sanjiangnan|sjn|2548@sjz|三井子|OJT|sanjingzi|sjz|2549@slc|双流机场|IPW|shuangliujichang|sljc|2550@slx|石林西|SYM|shilinxi|slx|2551@slx|沙岭子西|IXP|shalingzixi|slzx|2552@slx|双流西|IQW|shuangliuxi|slx|2553@smb|三明北|SHS|sanmingbei|smb|2554@smi|嵩明|SVM|songming|sm|2555@sml|树木岭|FMQ|shumuling|sml|2556@smu|神木|HMY|shenmu|sm|2557@snq|苏尼特左旗|ONC|sunitezuoqi|sntzq|2558@spd|山坡东|SBN|shanpodong|spd|2559@sqi|石桥|SQE|shiqiao|sq|2560@sqi|沈丘|SQN|shenqiu|sq|2561@ssb|鄯善北|SMR|shanshanbei|ssb|2562@ssb|狮山北|NSQ|shishanbei|ssb|2563@ssb|三水北|ARQ|sanshuibei|ssb|2564@ssb|松山湖北|KUQ|songshanhubei|sshb|2565@ssh|狮山|KSQ|shishan|ss|2566@ssn|三水南|RNQ|sanshuinan|ssn|2567@ssn|韶山南|INQ|shaoshannan|ssn|2568@ssu|三穗|QHW|sansui|ss|2569@sti|石梯|STE|shiti|st|2570@swe|汕尾|OGQ|shanwei|sw|2571@sxb|歙县北|NPH|shexianbei|sxb|2572@sxb|绍兴北|SLH|shaoxingbei|sxb|2573@sxd|绍兴东|SSH|shaoxingdong|sxd|2574@sxi|泗县|GPH|sixian|sx|2575@sxi|始兴|IPQ|shixing|sx|2576@sya|泗阳|MPH|siyang|sy|2577@sya|双阳|OYT|shuangyang|sy|2578@syb|邵阳北|OVQ|shaoyangbei|syb|2579@syb|松原北|OCT|songyuanbei|syb|2580@syi|山阴|SNV|shanyin|sy|2581@szb|深圳北|IOQ|shenzhenbei|szb|2582@szh|神州|SRQ|shenzhou|sz|2583@szs|深圳坪山|IFQ|shenzhenpingshan|szps|2584@szs|石嘴山|QQJ|shizuishan|szs|2585@szx|石柱县|OSW|shizhuxian|szx|2586@tan|台安南|TAD|taiannan|tan|2587@tcb|桃村北|TOK|taocunbei|tcb|2588@tdb|田东北|TBZ|tiandongbei|tdb|2589@tdd|土地堂东|TTN|tuditangdong|tdtd|2590@tgx|太谷西|TIV|taiguxi|tgx|2591@tha|吐哈|THR|tuha|th|2592@tha|通海|TAM|tonghai|th|2593@thb|太和北|JYN|taihebei|thb|2594@thc|天河机场|TJN|tianhejichang|thjc|2595@thj|天河街|TEN|tianhejie|thj|2596@thx|通化县|TXL|tonghuaxian|thx|2597@tji|同江|TJB|tongjiang|tj|2598@tlb|铜陵北|KXH|tonglingbei|tlb|2599@tlb|吐鲁番北|TAR|tulufanbei|tlfb|2600@tni|泰宁|TNS|taining|tn|2601@trn|铜仁南|TNW|tongrennan|trn|2602@tsn|天水南|TIJ|tianshuinan|tsn|2603@twe|通渭|TWJ|tongwei|tw|2604@txd|田心东|KQQ|tianxindong|txd|2605@txh|汤逊湖|THN|tangxunhu|txh|2606@txi|藤县|TAZ|tengxian|tx|2607@tyn|太原南|TNV|taiyuannan|tyn|2608@tyx|通远堡西|TST|tongyuanpuxi|typx|2609@tzb|桐梓北|TBE|tongzibei|tzb|2610@tzd|桐梓东|TDE|tongzidong|tzd|2611@tzh|通州|TOP|tongzhou|tz|2612@wch|吴川|WAQ|wuchuan|wc|2613@wdd|文登东|WGK|wendengdong|wdd|2614@wfs|五府山|WFG|wufushan|wfs|2615@whb|威虎岭北|WBL|weihulingbei|whlb|2616@whb|威海北|WHK|weihaibei|whb|2617@wlb|乌兰察布|WPC|wulanchabu|wlcb|2618@wld|五龙背东|WMT|wulongbeidong|wlbd|2619@wln|乌龙泉南|WFN|wulongquannan|wlqn|2620@wlq|乌鲁木齐|WAR|wulumuqi|wlmq|2621@wns|五女山|WET|wunvshan|wns|2622@wsh|武胜|WSE|wusheng|ws|2623@wto|五通|WTZ|wutong|wt|2624@wwe|无为|IIH|wuwei|ww|2625@wws|瓦屋山|WAH|wawushan|wws|2626@wxx|闻喜西|WOV|wenxixi|wxx|2627@wyb|武义北|WDH|wuyibei|wyb|2628@wyb|武夷山北|WBS|wuyishanbei|wysb|2629@wyd|武夷山东|WCS|wuyishandong|wysd|2630@wyu|婺源|WYG|wuyuan|wy|2631@wyu|渭源|WEJ|weiyuan|wy|2632@wzb|万州北|WZE|wanzhoubei|wzb|2633@wzh|武陟|WIF|wuzhi|wz|2634@wzn|梧州南|WBZ|wuzhounan|wzn|2635@xab|兴安北|XDZ|xinganbei|xab|2636@xcd|许昌东|XVF|xuchangdong|xcd|2637@xch|项城|ERN|xiangcheng|xc|2638@xdd|新都东|EWW|xindudong|xdd|2639@xfe|西丰|XFT|xifeng|xf|2640@xfe|先锋|NQQ|xianfeng|xf|2641@xfl|湘府路|FVQ|xiangfulu|xfl|2642@xfx|襄汾西|XTV|xiangfenxi|xfx|2643@xgb|孝感北|XJN|xiaoganbei|xgb|2644@xgd|孝感东|GDN|xiaogandong|xgd|2645@xhd|西湖东|WDQ|xihudong|xhd|2646@xhn|新化南|EJQ|xinhuanan|xhn|2647@xhx|新晃西|EWQ|xinhuangxi|xhx|2648@xji|新津|IRW|xinjin|xj|2649@xjk|小金口|NKQ|xiaojinkou|xjk|2650@xjn|辛集南|IJP|xinjinan|xjn|2651@xjn|新津南|ITW|xinjinnan|xjn|2652@xnd|咸宁东|XKN|xianningdong|xnd|2653@xnn|咸宁南|UNN|xianningnan|xnn|2654@xpn|溆浦南|EMQ|xupunan|xpn|2655@xpx|西平西|EGQ|xipingxi|xpx|2656@xtb|湘潭北|EDQ|xiangtanbei|xtb|2657@xtd|邢台东|EDP|xingtaidong|xtd|2658@xwq|西乌旗|XWC|xiwuqi|xwq|2659@xwx|修武西|EXF|xiuwuxi|xwx|2660@xwx|修文县|XWE|xiuwenxian|xwx|2661@xxb|萧县北|QSH|xiaoxianbei|xxb|2662@xxd|新乡东|EGF|xinxiangdong|xxd|2663@xyb|新余北|XBG|xinyubei|xyb|2664@xyc|西阳村|XQF|xiyangcun|xyc|2665@xyd|信阳东|OYN|xinyangdong|xyd|2666@xyd|咸阳秦都|XOY|xianyangqindu|xyqd|2667@xyo|仙游|XWS|xianyou|xy|2668@xyu|祥云|XQM|xiangyun|xy|2669@xzc|新郑机场|EZF|xinzhengjichang|xzjc|2670@xzl|香樟路|FNQ|xiangzhanglu|xzl|2671@ybl|迎宾路|YFW|yingbinlu|ybl|2672@ycb|永城北|RGH|yongchengbei|ycb|2673@ycb|运城北|ABV|yunchengbei|ycb|2674@ycd|永川东|WMW|yongchuandong|ycd|2675@ycd|禹城东|YSK|yuchengdong|ycd|2676@ych|宜春|YEG|yichun|yc|2677@ych|岳池|AWW|yuechi|yc|2678@ydh|云东海|NAQ|yundonghai|ydh|2679@ydu|姚渡|AOJ|yaodu|yd|2680@yfd|云浮东|IXQ|yunfudong|yfd|2681@yfn|永福南|YBZ|yongfunan|yfn|2682@yge|雨格|VTM|yuge|yg|2683@yhe|洋河|GTH|yanghe|yh|2684@yjb|永济北|AJV|yongjibei|yjb|2685@yji|弋江|RVH|yijiang|yj|2686@yjp|于家堡|YKP|yujiapu|yjp|2687@yjx|延吉西|YXL|yanjixi|yjx|2688@ykn|永康南|QUH|yongkangnan|ykn|2689@ylh|运粮河|YEF|yunlianghe|ylh|2690@yli|炎陵|YAG|yanling|yl|2691@yln|杨陵南|YEY|yanglingnan|yln|2692@ymi|伊敏|YMX|yimin|ym|2693@yna|郁南|YKQ|yunan|yn|2694@yny|云南驿|ANM|yunnanyi|yny|2695@ypi|银瓶|KPQ|yinping|yp|2696@ysh|永寿|ASY|yongshou|ys|2697@ysh|阳朔|YCZ|yangshuo|ys|2698@ysh|云山|KZQ|yunshan|ys|2699@ysn|玉山南|YGG|yushannan|ysn|2700@yta|永泰|YTS|yongtai|yt|2701@yta|银滩|CTQ|yintan|yt|2702@ytb|鹰潭北|YKG|yingtanbei|ytb|2703@ytn|烟台南|YLK|yantainan|ytn|2704@yto|伊通|YTL|yitong|yt|2705@ytx|烟台西|YTK|yantaixi|ytx|2706@yxi|尤溪|YXS|youxi|yx|2707@yxi|云霄|YBS|yunxiao|yx|2708@yxi|宜兴|YUH|yixing|yx|2709@yxi|玉溪|AXM|yuxi|yx|2710@yxi|阳信|YVK|yangxin|yx|2711@yxi|应县|YZV|yingxian|yx|2712@yxn|攸县南|YXG|youxiannan|yxn|2713@yxx|洋县西|YXY|yangxianxi|yxx|2714@yxx|义县西|YSD|yixianxi|yxx|2715@yyb|余姚北|CTH|yuyaobei|yyb|2716@yzh|榆中|IZJ|yuzhong|yz|2717@zan|诏安|ZDS|zhaoan|za|2718@zdc|正定机场|ZHP|zhengdingjichang|zdjc|2719@zfd|纸坊东|ZMN|zhifangdong|zfd|2720@zge|准格尔|ZEC|zhungeer|zge|2721@zhb|庄河北|ZUT|zhuanghebei|zhb|2722@zhu|昭化|ZHW|zhaohua|zh|2723@zjb|织金北|ZJE|zhijinbei|zjb|2724@zjc|张家川|ZIJ|zhangjiachuan|zjc|2725@zji|芷江|ZPQ|zhijiang|zj|2726@zji|织金|IZW|zhijin|zj|2727@zka|仲恺|KKQ|zhongkai|zk|2728@zko|曾口|ZKE|zengkou|zk|2729@zli|珠琳|ZOM|zhulin|zl|2730@zli|左岭|ZSN|zuoling|zl|2731@zmd|樟木头东|ZRQ|zhangmutoudong|zmtd|2732@zmx|驻马店西|ZLN|zhumadianxi|zmdx|2733@zpu|漳浦|ZCS|zhangpu|zp|2734@zqd|肇庆东|FCQ|zhaoqingdong|zqd|2735@zqi|庄桥|ZQH|zhuangqiao|zq|2736@zsh|昭山|KWQ|zhaoshan|zs|2737@zsx|钟山西|ZAZ|zhongshanxi|zsx|2738@zxi|漳县|ZXJ|zhangxian|zx|2739@zyb|资阳北|FYW|ziyangbei|zyb|2740@zyi|遵义|ZYE|zunyi|zy|2741@zyn|遵义南|ZNE|zunyinan|zyn|2742@zyx|张掖西|ZEJ|zhangyexi|zyx|2743@zzb|资中北|WZW|zizhongbei|zzb|2744@zzd|涿州东|ZAP|zhuozhoudong|zzd|2745@zzd|枣庄东|ZNK|zaozhuangdong|zzd|2746@zzd|卓资东|ZDC|zhuozidong|zzd|2747@zzd|郑州东|ZAF|zhengzhoudong|zzd|2748@zzn|株洲南|KVQ|zhuzhounan|zzn|2749'
url_request_img_code = 'https://kyfw.12306.cn/passport/captcha/captcha-image'
url_check_img_code = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
url_login_account = 'https://kyfw.12306.cn/passport/web/login'
url_login_check_one = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
url_login_check_two = 'https://kyfw.12306.cn/otn/uamauthclient'
url_init_travels = 'https://kyfw.12306.cn/otn/passengers/init'
url_left_ticket = 'https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT'

# 点击 预定 后发送的消息
url_user_status = 'https://kyfw.12306.cn/otn/login/checkUser'
url_order_ticket_one = 'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest'
url_order_ticket_two = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
url_order_ticket_three = 'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs'
# 点击 提交订单 后发送的消息
url_order_ticket_four = 'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo'
url_order_ticket_five = 'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount'
# 点击 确定 后发送的消息
url_order_ticket_six = 'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue'
url_order_ticket_seven = 'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime'
# url_order_ticket_eight = 'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue'


session = requests.session()
home_path = os.path.dirname((sys.argv[0]))

img_code_row = ['35','105','175','245','35','105','175','245']
img_code_col = ['35','35','35','35','105','105','105','105']
seat_index = {1:32,2:31,3:30,4:23,5:28,6:29,7:26}
seat_desc = {1:'商务座',2:'一等座',3:'二等座',4:'软卧',5:'硬卧',6:'硬座',7:'无座'}
seat_code = {1:'9',2:'M',3:'O',4:'4',5:'3',6:'1',7:'1'}

City = {}
CityR = {}
SecretStrs = {}

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>1
# 初始化、基本函数
def init():
	initCity(c_js)

	global from_station
	global to_station
	global queryDate

	file = open(home_path + os.sep + '信息表.txt','a+')
	file.close()

	file = open(home_path + os.sep + '信息表.txt','r')
	content = file.readline()
	file.close()

	content = re.sub("\n","",content)

	info = content.split('=')
	if len(info) < 5:
		print u'缺少必要信息，请先完善 信息表.txt。'
		exit()

	from_station  = info[3]
	to_station    = info[4]
	queryDate     = info[2]

	global Account
	global Password
	Account = info[0]
	Password = info[1]

	global goal_train
	global goal_seat
	global traveler_index
	goal_train = ''
	goal_seat = 0
	traveler_index = 0


def timerDelay():
	timer = threading.Timer(1,requestsLeftTickets)
	timer.start()

def getSplitChar():
	sysName = platform.system()
	if sysName == 'Windows':
		return '\\'
	else:
		return '/'

def inputNum(min_v, max_v):
	temp = min_v
	try:
		temp = input()
	except Exception as e:
		print u'输入错误，重新输入'
		return [False]
	
	if type(temp) == int and temp >= min_v and temp <= max_v:
		return [True,temp]
	else:
		print u'输入错误，重新输入'
		return [False]

def getANum(min_v,max_v):
	status = False
	while not status:
		temp = inputNum(min_v, max_v)
		status = temp[0]
	return temp[1]

def initCity(city):
	for S in city.split('@'):
		if not S:
			continue
		City[S.split('|')[1]] = S.split('|')[2]
		CityR[S.split('|')[2]] = S.split('|')[1]

def inputTrainInfo():
	global input_Trains
	print(format(u'','-^40'))
	print u'例如:k2276 g1890 k4792'
	print u'请输入期望的车次，默认全部'
	trains = raw_input()
	trains = trains.upper()
	input_Trains = trains.split()
	# input_Trains = ['G4314','G1874','G1862','G1882','G1894','G1870']

	if not input_Trains:
		input_Trains = ['K4808','K2278','T328']

def inputSeatInfo():
	global input_Seats
	input_Seats = []
	print(format(u'','-^40'))
	for index in seat_desc:
		print u'* %d:%s'%(index,seat_desc[index])
	print u'例如:5 4 6 3 2 1 7，多个按先后判断'
	temp = raw_input()
	temp = temp.split()
	for index in temp:
		if type(int(index)) == type(1) and int(index) >= 1 and int(index) <= 7 :
			input_Seats.append(index)
		else:
			print('ERROR 输入中存在错误，请重新输入')
			inputSeatInfo()
			return

	if not input_Seats:
		input_Seats = ['5']

def inputCheckInfo():
	checkInputStationAndTime()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2
# 请求验证码
def requestImgCode():
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		"Referer":"https://kyfw.12306.cn/otn/leftTicket/init",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	}
	data = {
		'login_site':'E',
		'module':'login',
		'rand':'sjrand',
	}
	response = session.get(url_request_img_code, headers = headers, params = data, verify = False)
	# 把验证码图片保存到本地
	with open(home_path + getSplitChar() + 'img_code.jpg','wb') as f:
		f.write(response.content)
	try:
		im = Image.open(home_path + getSplitChar() + 'img_code.jpg')
		# 展示验证码图片，会调用系统自带的图片浏览器打开图片，线程阻塞
		im.show()
		# 关闭，只是代码关闭，实际上图片浏览器没有关闭，但是终端已经可以进行交互了(结束阻塞)
		im.close()
	except:
		print u'图片错误或不存在'
		return requestImgCode()
# 验证验证码
def checkImageIds():
	#=======================================================================
	# 根据打开的图片识别验证码后手动输入，输入正确验证码对应的位置，例如：2 5  
	# ---------------------------------------  
	#         |         |         |  
	#    1    |    2    |    3    |     4  
	#         |         |         |  
	# ---------------------------------------  
	#         |         |         |  
	#    5    |    6    |    7    |     8  
	#         |         |         |  
	# ---------------------------------------  
	#=======================================================================

	imageIds = raw_input('请输入验证码位置 1~4 5~8，以空格分隔[例如:1 7]\n')
	answerIds = imageIds.split(' ')

	tempList = []

	for Id in answerIds:
		if type(int(Id)) == type(1) and int(Id) >= 1 and int(Id) <= 8 :
			tempList.append(img_code_row[int(Id) - 1])
			tempList.append(img_code_col[int(Id) - 1])
		else:
			print u'验证码坐标错误'
			return False

	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		"Referer":"https://kyfw.12306.cn/otn/leftTicket/init",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	}

	Code = ','.join(tempList)
	data = {
		'login_site':'E',
		'rand':'sjrand',
		'answer':Code
	}
	# 发送验证
	response = session.post(url = url_check_img_code, data = data, headers = headers, verify = False)
	result = json.loads(response.content)
	code = result['result_code']
	
	# 取出验证结果，4：成功  5：验证失败  7：过期
	print u'%s'%result['result_message']
	if str(code) == '4':
		return True
	else:
		return False
# 登录
def login():
	checkImgResult = False
	while not checkImgResult :
		requestImgCode()
		checkImgResult = checkImageIds()

	data = {
		'username':Account,
		'password':Password,
		'appid':'otn'
	}
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/login/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	print u'发送登录请求...'
	state = False
	while not state:
		try:
			response = session.post(url = url_login_account, data = data, headers = headers, verify = False)
			result = json.loads(response.content)
			state = True
		except Exception as e:
			pass
	print u'%s'%result['result_message']
	if result['result_code'] == 0:
		pass
	else:
		initAccount()
		return False

	# {"result_message":"密码输入错误次数过多，用户将锁定20 分钟,请稍后再试。","result_code":1}

	dada = {
		'appid':'otn'
	}

	print u'发送验证登录请求...'
	response = session.post(url = url_login_check_one, headers = headers, data = data)
	if response.status_code == 200:
		result = json.loads(response.text, encoding = 'utf8')
		print u'检查验证登录请求返回值...'
		print u'%s'%result['result_message']
		if result['result_code'] != 0:
			return False
		else:
			global newapptk 
			newapptk = result.get('newapptk')
	else:
		return False

	data = {
		'tk':newapptk
	}

	print u'发送确认登录请求...'
	response = session.post(url = url_login_check_two, headers = headers, data = data)
	if response.status_code == 200:
		result = json.loads(response.text, encoding = 'utf8')
		print u'检查确认登录请求返回值...'
		print u'%s'%result['result_message']
		if result['result_code'] == 0:
			print u'用户: %s 登录成功'%result['username']
			global apptk
			apptk = result['apptk']
			return True
		else:
			return False
	else:
		return False

def getTravers():
	print u'获取乘车人信息...'
	hander = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded',
		'Content-Length':'10',
		'Host':'kyfw.12306.cn',
		'Upgrade-Insecure-Requests':'1',
		'Referer':'https://kyfw.12306.cn/otn/index/initMy12306',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	data = {
		'_json_att':''
	}

	index = 1
	response = session.post(url = url_init_travels, headers = hander, data = data, verify = False)
	if response.status_code == 200:
		names = re.findall("'passenger_name':'(.*?)',", response.content)
		print(format(u'',"_^25"))
		for string in names:
			print u'序号:%d 名字:%s'%(index,string.decode('unicode-escape') )
			index += 1
		print(format(u'',"_^25"))

		global traveler_index
		traveler_index = getANum(1,index)
	else:
		print u'重新获取联系人...'
		# getTravers()

# 检查用户登录状态
def checkLoginStatus():
	data = {
		'_json_att':''
	}
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'If-Modified-Since':'0',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}
	response = session.post(url = url_user_status, data = data, headers = headers, verify = False)
	try:
		result = json.loads(response.content)
	except Exception as e:
		return checkLoginStatus()

	# {
	#     "validateMessagesShowId":"_validatorMessage",
	#     "status":true,
	#     "httpstatus":200,
	#     "data":{
	#         "flag":false
	#     },
	#     "messages":[],
	#     "validateMessages":{}
	# }

	if result['status'] and result['httpstatus'] == 200:
		if result['data']["flag"]:
			return True
		else:
			return False
	else:
		return checkLoginState()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>3
# 查询车次函数
def getStation(Station):
	try:
		Station = City[Station]
	except Exception as e:
		return None
	return Station

def checkInputStationAndTime():
	global from_station
	global to_station
	global queryDate

	from_station = getStation(from_station)
	if not from_station:
		print u'出发站错误'
		exit()
		return
	to_station = getStation(to_station)
	if not to_station:
		print u'到达站错误'
		exit()
		return

	timeArray = time.strptime(queryDate, '%Y-%m-%d')
	goalTime = int(time.mktime(timeArray))
	nowTime = int(time.time())

	if nowTime > goalTime + 86400 or nowTime + 30 * 86400 < goalTime :
		print u'日期错误'
		exit()
		return

def requestsLeftTickets():
	try:
		response = session.get(url_left_ticket%(queryDate,from_station,to_station))
		Data = json.loads(response.content)
		bHaveTicket = True
	except Exception as e:
		print u'没有查询到车辆信息'
		bHaveTicket = False

	text = ''
	global goal_train
	global goal_seat
	goal_train = ''
	goal_seat = 0

	#解析车辆信息
	if bHaveTicket:
		print(format(u' 检测时间： %s '%time.strftime('%Y-%m-%d %H:%M:%S'),"*^50"))
		for data in Data['data']['result']:
			trainInfo = data.split('|')

			if not SecretStrs.get(trainInfo[3]) and trainInfo[0]:
				SecretStrs[trainInfo[3]] = trainInfo[0]
			textmp = u'车次:%6s %+5s:%-5s %+5s-%s 共 %-7s 商务座:%s 一等座:%s 二等座:%s 软卧:%s 硬卧:%s 硬座:%s 无座:%s\n' %(
				trainInfo[3],CityR[trainInfo[6]],CityR[trainInfo[7]],trainInfo[8],trainInfo[9],trainInfo[10],
				trainInfo[32] or '--',trainInfo[31] or '--',trainInfo[30] or '--',trainInfo[23] or '--',trainInfo[28] or '--',trainInfo[29] or '--',trainInfo[26] or '--')
			text += textmp
			if not input_Trains:
				for s_id in input_Seats:
					tempInt = int(s_id)
					if goal_seat == 0 and trainInfo[seat_index[tempInt]] and trainInfo[seat_index[tempInt]] != '无':
						goal_train = trainInfo[3]
						goal_seat = tempInt
			else:
				for trainId in input_Trains:
					if trainInfo[3] == trainId:
						for s_id in input_Seats:
							tempInt = int(s_id)
							if goal_seat == 0 and trainInfo[seat_index[tempInt]] and trainInfo[seat_index[tempInt]] != '无':
								goal_train = trainInfo[3]
								goal_seat = tempInt

		if goal_seat == 0:
			timerDelay()
		else:
			print u'恭喜你，%s 车次 %s %s 有票'%(queryDate,goal_train,seat_desc[goal_seat])
			# 检查账户登录状态
			status = checkLoginStatus()
			if not status:
				print(format(u' 重新登录账户 ',"_^40"))
				result = False
				while not result:
					os.system('play ' + home_path + getSplitChar() + 'music.mp3')
					result = login()

			if SecretStrs[goal_train]:
				print(format(u' 开始预定车票 ',"_^40"))
				orderTicket()
			else:
				timerDelay()

	else:
		timerDelay()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>4
# 订票函数
def orderTicket():
	# 第一条消息
	print u'发送预定请求...'
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	# print(urllib.quote(SecretStrs[goal_train])) #编码
	# print(urllib.unquote(SecretStrs[goal_train])) #解码

	data = {
		'secretStr':urllib.unquote(SecretStrs[goal_train]),
		'train_date':queryDate,
		'back_train_date':time.strftime('%Y-%m-%d',(time.localtime(time.time() + 15 * 86400))),
		'tour_flag':'dc',
		'purpose_codes':'ADULT',
		'query_from_station_name':CityR[from_station],
		'query_to_station_name':CityR[to_station],
		'undefined':'',
	}

	response = session.post(url = url_order_ticket_one, headers = headers, data = data, verify = False)
	result = json.loads(response.content, encoding = 'utf8')
	if not result['status']:
		print result['messages'][0]
		# orderTicket()
		return

	# 第二条消息
	print u'获取票信息...'
	headers = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0'
	}
	data = {
		'_json_att':''
	}
	
	response = session.post(url = url_order_ticket_two, headers = headers, data = data, verify = False)
	initDcData = response.content

	REPEAT_SUBMIT_TOKEN = re.search("globalRepeatSubmitToken = '(.*?)';",initDcData).group(1)
	# print REPEAT_SUBMIT_TOKEN

	# 第三条消息 得到所有乘车人信息
	print u'获取乘车人列表...'
	headers = {
		'Accept':'*/*',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest'
	}
	data = {
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
		'_json_att':''
	}
	
	status = False
	while not status:
		response = session.post(url = url_order_ticket_three, headers = headers, data = data, verify = False)
		try:
			result = json.loads(response.content)
			status = result['status']
		except Exception as e:
			pass

	travelers = result['data']['normal_passengers']
	# print(format(u'',"_^25"))
	# for string in travelers:
	# 	print u'序号:%s %s 	%s  %s'%(string['code'],string['passenger_name'],string['sex_name'],string['passenger_type_name'])
	# print(format(u'',"_^25"))
	# print u'请输入一个乘车人序号'
	# traveler_index = getANum(1,len(travelers))

	session.get('https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=passenger&rand=randp&' + str(random.uniform(0,1)))
			
	# 第四条消息
	print u'提交乘车人信息...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	person = travelers[traveler_index - 1]
	item1 = []
	item2 = []

	# passengerTicketStr: 3,0,1,陈跃旗,1,410922198910122411,18039493069,N_3,0,1,李璐雪,1,410725199303202041,18336090658,N
	# passengerTicketStr: 3,0,1,陈跃旗,1,410922198910122411,18039493069,N
	# 座位编号,0,乘客类型,乘客名,证件类型,证件号,手机号码,保存常用联系人(Y或N(1个)/N_(多个))
	item1.append(seat_code[goal_seat])
	item1.append('0')
	item1.append(person['passenger_type'])
	item1.append(person['passenger_name'])
	item1.append(person['passenger_id_type_code'])
	item1.append(person['passenger_id_no'])
	item1.append(person['mobile_no'])
	item1.append('N')

	# oldPassengerStr: 陈跃旗,1,410922198910122411,1_李璐雪,1,410725199303202041,1_
	# oldPassengerStr: 陈跃旗,1,410922198910122411,1_
	# 乘客名,证件类型,证件号,乘客类型
	item2.append(person['passenger_name'])
	item2.append(person['passenger_id_type_code'])
	item2.append(person['passenger_id_no'])
	item2.append(person['passenger_type'] + '_')

	passengerTicketStr = ','.join(item1)
	oldPassengerStr = ','.join(item2)
	# print passengerTicketStr
	# print oldPassengerStr

	data = {
		'cancel_flag':'2',
		'bed_level_order_num':'000000000000000000000000000000',
		'tour_flag':'dc',
		'randCode':'',
		'whatsSelect':'1',
		'_json_att':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
		'passengerTicketStr':passengerTicketStr,
		'oldPassengerStr':oldPassengerStr,
	}

	response = session.post(url = url_order_ticket_four, headers = headers, data = data, verify = False)
	result = json.loads(response.content)

	if not result['status']:
		print u'%s'%result['messages']
		timerDelay()
		return

	# 第五条消息
	print u'获取订单队列...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	train_date = re.findall("'time':(.*?)000,",initDcData)
	train_no = re.search("train_no':'(.*?)'",initDcData).group(1)
	stationTrainCode = re.search("station_train_code':'(.*?)'",initDcData).group(1)
	leftTicket = re.search("leftTicketStr':'(.*?)',",initDcData).group(1)
	train_location = re.search("train_location':'(.*?)'",initDcData).group(1)
	purpose_codes = re.search("purpose_codes':'(.*?)'",initDcData).group(1)

	# print train_date
	# print train_no
	# print stationTrainCode
	# print leftTicket
	# print train_location
	# print purpose_codes

	data = {
		'train_date':time.strftime('%a %b %d %Y %H:%M:%S GMT+0800 (%Z)',time.localtime(float(train_date[len(train_date) - 1]))),
		'train_no':train_no,
		'stationTrainCode':stationTrainCode,
		'seatType':seat_code[goal_seat],
		'fromStationTelecode':from_station,
		'toStationTelecode':to_station,
		'leftTicket':leftTicket,
		'purpose_codes':purpose_codes,
		'train_location':train_location,
		'_json_att':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN
	}


	status = False
	index = 1
	while not status and index < 5:
		try:
			response = session.post(url = url_order_ticket_five, headers = headers, data = data, verify = False)
			result = json.loads(response.content, encoding = 'utf8')
			status = True
		except Exception as e:
			index = index + 1
		
	if not result:
		print u'获取订单信息错误，重新查询'
		timerDelay()
		return

	# 第六条消息
	print u'确认订单...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}

	key_check_isChange = re.search("key_check_isChange':'(.*?)',",initDcData).group(1)

	data = {
		'randCode':'',
		'purpose_codes':purpose_codes,
		'passengerTicketStr':passengerTicketStr,
		'oldPassengerStr':oldPassengerStr,
		'seatDetailType':'000',
		'whatsSelect':'1',
		'roomType':'00',
		'dwAll':'N',
		'_json_att':'',
		'choose_seats':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
		'leftTicketStr':leftTicket,
		'train_location':train_location,
		'key_check_isChange':key_check_isChange,
	}

	response = session.post(url = url_order_ticket_six, headers = headers, data = data, verify = False)
	result = json.loads(response.content, encoding = 'utf8')
	if not result['status']:
		print u'%s'%result['messages'][0]
		timerDelay()
		return

	# 第七条
	print u'获取订单编号...'
	headers = {
		'Accept':'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding':'gzip, deflate, br',
		'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
		'Connection':'keep-alive',
		'Host':'kyfw.12306.cn',
		'Referer':'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
		'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:34.0) Gecko/20100101 Firefox/34.0',
		'X-Requested-With':'XMLHttpRequest',
	}
	data = {
		'random':int(round(time.time() * 1000)),
		'tourFlag':'dc',
		'_json_att':'',
		'REPEAT_SUBMIT_TOKEN':REPEAT_SUBMIT_TOKEN,
	}

	times = 1
	status = False
	orderId = ''

	while not status and times < 5:
		try:
			response = session.get(url_order_ticket_seven, headers = headers, params = data)
			result = json.loads(response.content, encoding = 'utf8')
			if result['data']:
				if not result['data'].get('orderId'):
					if result['data'].get('msg'):
						print result['data']['msg']
					else:
						print u'返回错误,重新获取'

					time.sleep(1)
				else:
					orderId = result['data']['orderId']
			status = True
		except Exception as e:
			times += 1

	if orderId != '':
		print u'订票成功 订单号: %s，请于30分钟内付款'%orderId
		suucessTip = Image.open(home_path + getSplitChar() + 'success.jpg')
		suucessTip.show()
		suucessTip.close()
		os.system('play ' + home_path + getSplitChar() + 'music.mp3')
		exit()
	else:
		# print u'请登录12306查看未完成订单详情'
		# errorTip = Image.open(home_path + getSplitChar() + 'error.png')
		# errorTip.show()
		# errorTip.close()
		print u'unknown error, try it again !'
		timerDelay()
	
