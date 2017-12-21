
package y2017;

import java.util.*;

public class Day04 {

	public static void part1() {
		Scanner readInput = new Scanner(INPUT);
		int count = 0;
		while (readInput.hasNextLine()) {
			Scanner line = new Scanner(readInput.nextLine());
			boolean valid = true;
			Set<String> words = new HashSet<String>();
			while (line.hasNext() && valid) {
				String word = line.next();
				valid = !words.contains(word);
				words.add(word);
			}
			line.close();
			count = (valid) ? count + 1 : count;
		}
		readInput.close();
		System.out.println(count);
	}

	public static void part2() {
		Scanner readInput = new Scanner(INPUT);
		int count = 0;
		while (readInput.hasNextLine()) {
			Scanner line = new Scanner(readInput.nextLine());
			boolean valid = true;
			Set<String> words = new HashSet<String>();
			while (line.hasNext() && valid) {
				String word = line.next();
				valid = !setContainsOrAnagrams(word, words);
				words.add(word);
			}
			line.close();
			count = (valid) ? count + 1 : count;
		}
		readInput.close();
		System.out.println(count);
	}

	public static boolean setContainsOrAnagrams(String word, Set<String> words) {
		boolean result = false;
		if (words.contains(word)) {
			return true;
		}
		for (String current : words) {
			result = isAnagram(word, current);
			if (result) {
				break;
			}
		}
		return result;
	}

	public static boolean isAnagram(String a, String b) {
		if (a.length() != b.length()) {
			return false;
		}
		for (int i = 0; i < a.length(); i++) {
			if (b.indexOf(a.charAt(i)) == -1) {
				return false;
			}
		}
		for (int i = 0; i < b.length(); i++) {
			if (a.indexOf(b.charAt(i)) == -1) {
				return false;
			}
		}
		return true;
	}

	public static void main(String[] args) {
		part1();
		part2();
	}

	public static final String INPUT = "nyot babgr babgr kqtu kqtu kzshonp ylyk psqk\r\n"
			+ "iix ewj rojvbkk phrij iix zuajnk tadv givslju ewj bda\r\n"
			+ "isjur jppvano vctnpjp ngwzdq pxqfrk mnxxes zqwgnd giqh\r\n"
			+ "ojufqke gpd olzirc jfao cjfh rcivvw pqqpudp\r\n" + "ilgomox extiffg ylbd nqxhk lsi isl nrho yom\r\n"
			+ "feauv scstmie qgbod enpltx jrhlxet qps lejrtxh\r\n"
			+ "wlrxtdo tlwdxor ezg ztp uze xtmw neuga aojrixu zpt\r\n" + "wchrl pzibt nvcae wceb\r\n"
			+ "rdwytj kxuyet bqnzlv nyntjan dyrpsn zhi kbxlj ivo\r\n" + "dab mwiz bapjpz jbzppa\r\n"
			+ "hbcudl tsfvtc zlqgpuk xoxbuh whmo atsxt pzkivuo wsa gjoevr hbcudl\r\n"
			+ "gxhqamx dradmqo gxhqamx gxhqamx\r\n" + "yvwykx uhto ten wkvxyy wdbw\r\n"
			+ "kzc ndzatgb rlxrk hfgorm qwgdky ndzatgb rhvyene qaa wxibe qwmku nmxkjqo\r\n"
			+ "qwx ubca dxudny oxagv wqrv lhzsl qmsgv dxs awbquc akelgma\r\n" + "rrdlfpk ohoszz qiznasf awchv qnvse\r\n"
			+ "ggsyj czcrdn oolj sibjzp ibzjps asp\r\n" + "vbcs ypgzae xcvpsr ptvb leoxqlq zmpt fhawu yfi tvbp\r\n"
			+ "ejkr qlmag nsz jwpurli nhsml asksnug mes\r\n"
			+ "kkgkjml kklmgjk kjgpx iquytbj eccceb mfv iuyqjbt ovv\r\n" + "uoklkco zzey sdfhiyv ytdeg\r\n"
			+ "azr mjv raz arz rdfb\r\n" + "pir dafgsah dafgsah kndjbml estcz yjeoijp kkcws ebq puwno\r\n"
			+ "iqymwc tac vlqc bmnkz xustm leqi\r\n" + "gwdjed cfha axz xjuq\r\n"
			+ "abfjsg pahat qlj zan qsfn iozfys jnvu bis jakggq\r\n" + "afwuejn zrbu zurb hrn lwvjb jnwixla aufejnw\r\n"
			+ "vkqn cuzf humhriz webnf uzfc zfuc\r\n" + "eznxd kgbfy jqyc net vzfege tprzyc\r\n"
			+ "mqnapzn vrgw ilzp vgw\r\n" + "aie zkkih fhpwu bbn fhpwu wvxxgmd\r\n"
			+ "ksoasrn yll mvdjxdo wydymx dmodvjx drnjlm tcjpjhj xzakb wrsbuwl vaygdwf rsasonk\r\n"
			+ "qahbh tfhkl apdqqpm tfhkl nsox\r\n" + "xkelwve mvdmesj xrto tgku gkb bpe\r\n"
			+ "nni nyylpu cyusxe zydeyok yokzdye xiscesy\r\n" + "itwsfr eqwrx igqkvif whklwdb\r\n"
			+ "lpa hwci suwqfln xis sfht lzek ajecd\r\n"
			+ "svpf eulute eya gvmsd app claria tjtk zjt agdyemi bixewo\r\n"
			+ "gmzglxi zlgouy bejg kte xlf giquj mjeq ivjkw ktbhaga hoffyrt\r\n"
			+ "wwjy dtf ftd agei yde xhbfo fyridy\r\n" + "gexcy hetkz ufflrfi frifluf plb kqre etxo elg henqy fspm\r\n"
			+ "khaemn buec ichau wxctsxg\r\n" + "cgmv ujyvcuu jta yux ccx skrafkn cmyc yidqhv ltb ycnajry zitq\r\n"
			+ "ybsahqn pio veeze vdztjz iedou pio sue ijbz gvqncl vpa ijbz\r\n"
			+ "hkfi xzrsyke hikf mxolx xlxmo ungfc tst xjzd\r\n" + "tpx ioprco qixlv ipocro\r\n"
			+ "oahmwrv homvraw vws ntmbdvx\r\n" + "fxlg wnuz ogt bxgtul vmfh nwuz glfx tgxdq bxfv kajuh\r\n"
			+ "vrhqn nrqvh tgogb vya ragbro ulrz uava kexoi yav vkfe\r\n"
			+ "bxxy tyxgxd oabsud bauosd jlch bdmrqq wqhjwb ayblb hclj\r\n" + "sfzsgsc sfzsgsc jbrvh sfzsgsc bdhy\r\n"
			+ "wixleal vhnqbfw qwfnhbv woco oowc\r\n" + "exkkwz wekxzk krxbua nshxqgh\r\n" + "gkn blxgui nkg gnk\r\n"
			+ "otsa isqn otsa isqn\r\n" + "ude xedl ude xedl amkktp\r\n" + "teroe yuvbd inf mpytuvz xiq xqi ovqetn\r\n"
			+ "zyq ybeifwx fvoqp vhoduy bcq wbxl\r\n" + "zymiid vafcqv vjbmekf lgxkma bjti qfavcv iqp fnbu lakmgx\r\n"
			+ "rkaqvd vylkh jfdxh imxxg bbrt imxxg rkaqvd\r\n"
			+ "yajg qnhhs bzmb eyk hijcg tkij iwr jvwp dipzd jvwp\r\n"
			+ "btzhw zttheyo ravsbz bmbba majoe ykrs tbxqf tai cgsvpu srbavz\r\n"
			+ "vsyczfs ymg vsyczfs wxlwaqb oouio owek wxlwaqb azvbqiq\r\n" + "ghrapd ghrapd wisq wisq\r\n"
			+ "znmleu aztnkbs wxc gycxd vqenhh geqyo rpjg\r\n" + "kxbom gzz zzg zgz\r\n" + "dfsesc okwb dfsesc okwb\r\n"
			+ "egpwqbe djlk xpkxa hoo eepbqwg\r\n" + "nxdfror yfhkhn zgea fkspva rjgg bnmq ddsf rjgg gkinm\r\n"
			+ "vdrxfom wbdwu dhkt xtvzc zjobo aqvgrt\r\n"
			+ "svddsgz mhcrbcp wmpd mhcrbcp klim ddlnxv wrdftrc ddow wrdftrc\r\n"
			+ "obxr wscs new brxo wen epns cvjvxts ilnc\r\n"
			+ "rwezl vmbut kgblt xfg vnhlebq nzqdzxm ynh wokrezy zub nzzqxdm\r\n"
			+ "vephajp bzupele mltzglh sbgn vephajp lhve mltzglh\r\n"
			+ "slajp kyaf vlnvy srfietn ayfk inaufex fanuexi\r\n" + "vazwg kjg qanzso ptuu vvlwq uupt kohhql jkg\r\n"
			+ "xmmmpky rbqimi slvxsf tlcwm pbf pks iucx rbmiqi\r\n" + "irkup jvu tkeioz avdu suxamf\r\n"
			+ "tmgih ldca jswka dblzzt rap rgqyy gyrqsk nnnn pok\r\n"
			+ "pdbjhrl gsvxbqr nqfkhtc ngn okbgzd pdbjhrl oostjtm okbgzd\r\n"
			+ "mzqfdat dujh aeplzqh acbguic vlzdt amyszu amyszu jqecky bhl hjqnimq xoy\r\n"
			+ "dszafr bqampg epozj sfrlpe dszafr wfurku sotjpg wagtnxy\r\n" + "jbmo jbmo plbfkvw bkc jbmo\r\n"
			+ "ehelldu vrid unnf vrid xqiu tbibjyi bmbpsmq tpqyefx xqiu\r\n"
			+ "rpgm zzbj cjgfdyb bdjfgcy rzqecd miyvfbu aqlkagf hsuxwgl\r\n"
			+ "gvywzp phvnd ypwypbm yfelxx egbr lcfyz hecdhkj xxfley\r\n" + "tsmebin tbsnmie mkijj ijjmk\r\n"
			+ "cghxrqs vzxle wrfghv skighgt zviteab plcrgv\r\n" + "ezdirp rxkw horcek qcgny inx nikb tigzp\r\n"
			+ "eidk sactjci sre vkapava owvf eyds eyds\r\n" + "vvjdm uye tjixj azklizl pnb\r\n"
			+ "tcrimv xye twii xye twii tad\r\n" + "mtxcg lwjxdj zjudqu ekoujd ysf ajtfta dkj lwjxdj\r\n"
			+ "aowhmvv kkic kjize fnohl ukx remfmii usbp\r\n"
			+ "wkossu limxmhp xnoeocb wkossu lnrlqf kjozfg xeulstx sjncsw ekaimuv xnoeocb sxjegcg\r\n"
			+ "lsfe zpewzlc yhjyiay lou ukhi lpwezzc slef zvtidgg kdeseq enka tfvgudr\r\n"
			+ "ovfsa vuv tbtorv tbtorv gmxn opspw lli mfzvkv zlyhr oznalr\r\n"
			+ "kugrpw sduq rdc ciaxwir ylnzwec kugrpw sduq\r\n"
			+ "obevuau thu jpyfvof rpawwo obevuau gsvoutr quiaei\r\n" + "xpgua pbxa pxgau kdan\r\n"
			+ "ohyzqk abxgg xozgai nib axozig bni fucgykm jpkswt\r\n" + "jrgu dmozts jrug ufpho\r\n"
			+ "qojzue uzeojq txuhj eqjzou\r\n"
			+ "wcvj qwlravl niyxf oiaptlk wlxnnzj jgdzap jgdzap lfgn bdt sfga adrypo\r\n"
			+ "ylah eedu rvwdpmq eedu ylah\r\n" + "quages kmla yjqua dzxcfam srjag wujmcv qujya ssaol uzdwi\r\n"
			+ "gdsppz yqxlish yfkjbbf ecnzu ejvtv cdjwre\r\n"
			+ "slsls pcmrq zax btrc kliv ntho gymkk kkq pcrmq mvnw sjfegpx\r\n"
			+ "ryz jfw eki wvibww qdzylg whbagp ffrfjg wdhnqpm hcrz\r\n" + "tcjqfh tmvzp mpztv vpmzt\r\n"
			+ "xood xutgof teqov fqyyub oakm rzaheiq\r\n"
			+ "axagoq jawbz sexucp sexucp atenr edekcwn edekcwn agl ecj gbje gipivfq\r\n"
			+ "poqv qopv bos flhghs gshlfh\r\n" + "rxd dzphnb bwmna vxd rxd sbk kuor\r\n"
			+ "kqeelq jqbyh xczqzqe jbkmx kelqeq xqcfqn\r\n" + "jdfy qzjyz xvqyo jdfy xvqyo\r\n"
			+ "vyoqyd pwayqag eygmdt smakwc veftikz fzeikvt\r\n"
			+ "aozgkne mpd mktgoew eepp zlwycr eepp hswbxcx nmi ddnfr eepp\r\n"
			+ "dgpfp cfhhqdx vjrb uyimbm byx hfdhxqc\r\n" + "fxq jcouwfy uhuao zsab xjao\r\n"
			+ "noudveu egxyuqw hmnnv vovt wmqkx syatiac whkd\r\n"
			+ "gxyzk opgb kjxp delavq hsnvk kfn irkcfq lvc aadcwy opgb\r\n"
			+ "exuiupk ddiiyvm nsggpj ddiiyvm nsggpj\r\n"
			+ "hhjby rfejzp akxzs nconlt rynivtq voloj qwhhll ubvx yxuacz miuwxh ppe\r\n"
			+ "uspqvx supvxq cekv niddfuw\r\n" + "optzcag sra ajs ozacptg yxkludq jjpvldz mxo mox\r\n"
			+ "dko qyec iuxbrbj dlz jxribub\r\n" + "ywlyz vipfh amsfr fwiozi tahjov tap rsea zwlyy oqdyfbo\r\n"
			+ "xeqml jwy eguc bvzvh\r\n" + "crp mxsihvo wwtg gsypx mxsihvo qpfw looca gewvy zjqki tdkuxo crp\r\n"
			+ "mqlnzm yihsvrl hhtwcv kigymqu yswki hksk vbiujq xeqz irzcq cpnz\r\n"
			+ "zxhfsw uuyhwid nzabem mmfk wszfhx shxzwf hqnrvsq\r\n" + "hfjajdl qwmk hjdalfj mwkq gqbku dsszk\r\n"
			+ "fbiy pujq htgaqqq yro ztpe yiufb fnpi ggchdgz\r\n"
			+ "sixq jsboan eoie msdrwzw sixq njsrc sixq yimqoi\r\n"
			+ "pbxgv kqmi hjuk bbtrlta bqwm bgehofj ainqhm qoypsil manhiq ogebhfj lvmuo\r\n"
			+ "wnax aen fthpcke tcz yadjmva mydavaj rcfkc krfcc\r\n"
			+ "lkatiw zxliii usdj oopxl yylv bkjfy gtlyjv usdj muqazdb\r\n"
			+ "yqonaxv wqnvoo hfpll oyxnlfs fgajc khhtzr hfpll gsvvipz wbjxsnp dcdikt hqw\r\n"
			+ "vvuv kspmnz zvmryqd egvuz eazkhz kspmnz\r\n"
			+ "xgq dziwiym gsl nbzmsta ccbzn yalof dbbugq aar ywmbvk yofla dcwb\r\n"
			+ "qrtyhhw xeyo vlym ulzzbl hrxyb qeyu jqdkewk oxye evaxz kybc bssyt\r\n"
			+ "eqrf cfyy kwhohw ozg jsc egz jsc\r\n" + "vct cet ixxvmz ibhvndq eks dpi jzfwdqv saeh jqzdfwv vwfdqjz\r\n"
			+ "vus vus kitvvgq wpi alfncf gzj oxcy fith oxcy ecbsr\r\n"
			+ "uacculk guwhwdp cankcv yswy bmby sve dvonm nran\r\n" + "ydftm wszgaex rgbw otd dbet lhsxndd jqfyx\r\n"
			+ "vhawg hwagv uagy fveik nrsew zujw hawvg dzfmt agzgw\r\n" + "uqdj talb uqdj aizyuqm\r\n"
			+ "pbbejee szdtohv tycfow xwne qzlqy dxcwejz pqdqrc wfyotc gdqt uxaeug wtldm\r\n" + "hmzmd oyp pyo opy\r\n"
			+ "qwdh kwpll kwpll zsbez uxg klr uxg\r\n" + "myqr zza kqpcos adsql eumunrv qlaeumx\r\n"
			+ "acyye xvdewe nwkhuz bzcmx asw ostiwk mfzu nwkhuz\r\n"
			+ "memq uqadd kfj dses lrxb hxygp dsse bxbr hgpxy uavrar\r\n" + "mjmk lsdttuz qjkg yfthmkn pram\r\n"
			+ "pctfq aly usim shihap uims xkfgp ksrbn ifvsyl\r\n" + "cdma nnnu hdm dhm\r\n"
			+ "kpt upgsm ohvrrqf qwps wjcbve ohvrrqf\r\n" + "wowphgb nteme otizypb eumgvb puoctli opicult wbohwpg\r\n"
			+ "fppz ftkql sbut lkqtf svif viqhlnn buts lljhbd\r\n"
			+ "oqk uinby rqy vbjhf oul hzfo coca glpy brjy yglp qnvhvei\r\n"
			+ "sbbwr dnyrux gpikv nsx aawyeq uhtucwq rhxzy jgx bdgdrl dnyrux lgfgi\r\n"
			+ "agn mljz hgmglem popu jtapub agn\r\n" + "ehfpgr bnobvg bnobvg bnobvg\r\n" + "ozgzedn godezzn art atr\r\n"
			+ "urz rzu xzyc rjhwi kgiodi doiigk layr dwbxu\r\n"
			+ "rkcbav pnp bpsmm ifivfe csouqpw fyswzbd csouqpw bnjt rnnoxed\r\n" + "hpjgtcc ctcpgjh cchjtgp lxn\r\n"
			+ "cinokbx uyaz uyaz uyaz\r\n" + "bphfwad bphfwad bphfwad yml izlhlb dvjvo jeropar\r\n"
			+ "ocgftcl wshjk zbinw fcotlgc xdj nwibz\r\n"
			+ "zbze hllno rmq invd gupoxr gwumc vnzj fcvvhjo dnn sfsxw\r\n"
			+ "oqlhkz hgf yxiahks vhzvl ayshkxi irmwkmq\r\n"
			+ "apeqic ahwu abxjrd tuwrd pynnil eohmlgo lafx ybpofe wbznxv swuafas\r\n"
			+ "cpg jpsfo jposf rer ixeydpz\r\n" + "rhqrwvn wrhqnrv xptms jhc rnqvhwr\r\n"
			+ "zfpl tukxzda lifkqtd ynfuno cttx ctxt tlqdkfi ueswv wbipfbe\r\n"
			+ "eblw bwbjg fuu qqm qtv qtv isbl denfcb\r\n"
			+ "ick yqwcffk pvcchd apkjyc ouu uyfe nplid ick caqscs sddkx\r\n"
			+ "rtzh idn snnw xmlou idn kdhenl rtzh ujwttl pkynkhe\r\n" + "dnwha fpv dnwha iqi xggepo dnwha\r\n"
			+ "yjvk saay enxqhw wigoah dzasyr nnt artl iqwia jpp xmfr hwigao\r\n"
			+ "ryt heenuai ytr gqew hyb byh wdurx kmd adgjz\r\n"
			+ "ypdqeji sfkkfhn stms cdmyh nqllx utiphia gxbx zflhtgo yurztx eni\r\n"
			+ "pwlhlt lhlwpt rfkvlgr tucajej ckujc ntcyae xestygt eshmggk\r\n"
			+ "gtfb codwc vjtli ffmjwx ruoekt cylrm ktroue dfaxzvs kkgejzi ewucgu jyatrum\r\n"
			+ "ersbag cod xssha aqzbe kxu bzghhqk pbs bizvqk bhbbd bps\r\n"
			+ "vhci ypxf bxzor unngl xilpzpk civh nykora vchi\r\n"
			+ "cyb cceu negnld nbcfs pxsjgh xah nbcfs nbcfs jabpxg wtanv qhztvr\r\n"
			+ "cljgzkn lrdeina hrjoz kdgpn vqkmpal nivk scvnu vzuausp\r\n"
			+ "nif fin uxjbip xxztsn yyo opueh zxs qnso paedey hsd fttvqdn\r\n" + "gbnkmpr afo aof ryyudy gbmpnrk\r\n"
			+ "uaa npb dkit npb buadan esv npb hwrj\r\n" + "hws dfgq fcyty qszhu chyxxl ytmpb azxl jrsn boqrx\r\n"
			+ "hkzlnkd fkilvog xbubu fbgbp\r\n" + "fgi inmay uliytc vgkcw qsoe uliytc isjhix oyir ocaq\r\n"
			+ "qrzkpm dpzetbr zommsxo cixg nwjyvp bet wyjpvn cgxi tsncd\r\n" + "uvlf lufv ulfv cigl\r\n"
			+ "uwwf thr kdq fhjmty bvxue vcwwmk kdq nzajq bxkf\r\n" + "qcwduju idxaja qcwduju idxaja\r\n"
			+ "fnarz pstzfne nco qzf kcevoo qwx csvsxga pstzfne\r\n" + "twug xrwy uoctfl bkh yxrw\r\n"
			+ "unpdnbe apf cvm bpullu fyels tjpri jyw unpdnbe xfyekay vhk zpyb\r\n"
			+ "rbv psirdv psirdv mnjrp qpwc vicismd qpwc\r\n" + "zjj zjj kesyhow eqcfqy vqy\r\n"
			+ "zazpd gmea aobl dcs mage hqjdpwc bvxr srw\r\n" + "rhcdb nzsa jgcgc rhcdb wxs vsvvptn zvckqo wxs\r\n"
			+ "unyet prchn fiwter wvgknes dvzbxfs ufet neuyt fczlrx bpocdci vdsfzbx\r\n"
			+ "znfev fwrdarx knqkv ojiv ojiv fwrdarx\r\n" + "tbtlo hdashg kyspxm ypmkxs nmrk\r\n"
			+ "fzr zqxaszt frz xzrre\r\n" + "shueb iraetk uhsv duvah uhsv zstysc nrfllbc emrknka\r\n"
			+ "vzkrmp mgtkjnw njr bwjgp jdwyyhv yudha wbvmx ewu urhiioq\r\n"
			+ "yjq xxr swvm aipdj apjid tfsq gfqg izrvhev\r\n" + "iljuqt fpo fxadit iljuqt iljuqt\r\n"
			+ "zrj poewso vsje bsprbmc vsje yfwf ybu dmkqib ybu hlrpdi ymh\r\n"
			+ "apxaeq bgdm mqty whyay mnuzfgk awm bgdm mwwi ekw bgdm\r\n" + "dpdbfkm crrg mkph kphm grcr ukbk\r\n"
			+ "ilqm wroz mqil qlim\r\n" + "pnlx nwadw uabelu rueamxr wjer uwge jwer ywagrx\r\n"
			+ "akuil nkh oitq werli werli\r\n" + "fkmhcr ieoj xfsa xfacoeb tcg poomcme vck zmpc djcqgkf kft\r\n"
			+ "csyk qni hqfrye zyyxz ggynzad pjpokmu bigqa qie\r\n"
			+ "lkpenw zyllii qtbvdq zqnu ichftg xazped agl irhlbiy snlwfe twliar\r\n"
			+ "acsrba dzz ivylbl rfcdd rfcdd qcg\r\n"
			+ "zbui fomvpx zjhmgl sivtffu xuhswzt fzeid tgj mzok mozk afbhuje tzswxuh\r\n"
			+ "nupjiat fdxkbn tuatp jhdfnub yitdk yghqw nupjiat ibi edfv tuixw auwjm\r\n" + "focht mnprh tljj ayp\r\n"
			+ "pjdnl uaoworh iqm gic dqlu spn heuymio\r\n" + "kvg ferrvhp unvzsd qdcpd rji zpch\r\n"
			+ "nhvay chuzg pyhdd hnmrnq zeidhf pyhdd ohy hnmrnq\r\n" + "boa sau gxh grx\r\n"
			+ "gwo utwpd zcsrx gow bnm\r\n" + "xoqniyd hmithl xoqniyd hmithl\r\n"
			+ "yqqsbzo stca zcsjnqf skbueeu tlbkef mvqbg igzr wujuz yqqsbzo kkfe\r\n"
			+ "wgzuepu wge fkrxuag csenx tkngoz wge azueyxs\r\n" + "get xiryxs xiryxs xiryxs\r\n"
			+ "wammvx edy hahetl xmvawm dye\r\n" + "lscxxgi anmax quo cqprwn imocarq gnbfhe rcnqpw\r\n"
			+ "znpmid yaluvzn ydm ckh uhso rrk wbby lwxsu\r\n" + "atppk byf dzz uift nqejgm njgeqm\r\n"
			+ "dtqmy iog ahub habu\r\n" + "hkthdwt pfxlwsu hkthdwt hkthdwt\r\n" + "tsuiue tsuiue yais tsuiue\r\n"
			+ "swooqmp rqrcs ngr vujrq inuu rqrcs\r\n" + "dhu zxdfiyv xuz xuz mgaty mgaty\r\n"
			+ "kiiiz zco qdv vfgkj rders zco\r\n"
			+ "trszp havbm redpeqk gktp ifvzvwl yfoxnm tzg avzd otiouso eks lqlutwb\r\n"
			+ "cfiru lpdy kpeas mdc lxnjjqz nqyyb xkjsug rcifu dln\r\n"
			+ "jga ijgkjo qhbnupb ofzqn iokjjg gaj lrh pkynrcr jgatk\r\n" + "bexwc tat tat otsngaa\r\n"
			+ "feh mjxbs ehf cyfhlv vvdgdu hef\r\n"
			+ "njlvq ojwaes awsejo ktyvxd qeyeze bpoaj ulgngn zyeqee kqc bsdzzvq\r\n" + "hbfp vnhs vnhs pko pxnxgm\r\n"
			+ "bmy bzpn bzpn bcfep\r\n" + "cju nqjy yjqn bbrj esgzw swgl bjrb\r\n"
			+ "cxvrshm rbglkyv kqwzcyd azqr ckwbbew fhgqv nfk lactzh ssqpwbr wbewbck\r\n"
			+ "ptcb gqkb apcc okl jbbgk qni bqu slydyo qhh dqd osv\r\n"
			+ "zbisefn bmxcljk bmxcljk arkamus vpq uxuwvb\r\n" + "ksik xbzk lahh ctfur sxh rduokr xqou zwbgqsp skik\r\n"
			+ "hwhmfk hwhmfk bjpxzg qqftmu ijyv igvayf bjpxzg\r\n" + "askxqew tibx pqaczy fhzyec echzfy cezfhy\r\n"
			+ "omzyy mbzfvsn kkoff qgqn crnnkn krx oqp jhn anb qte qxt\r\n"
			+ "jypnwn vjbnbsl axf pldxbq pdoy rmxcvig cpad yhah rzqewkg nmzkkr erjo\r\n"
			+ "visidzp bujlfn xuomjj mjnqn wgflg skb\r\n" + "oer oer lfi zyqnem lfi guljz\r\n"
			+ "fannhwu wafma gcje cvcia qwyh ugtbpa geufqg\r\n" + "kwtjib pqwai tdmjj kuxr euzl rxuk\r\n"
			+ "ovi splc hflutgw hflutgw\r\n" + "gvel gelv aeiygth elvg twwr kivxrrj jkmqa\r\n"
			+ "bas ylxbdgn yliv pytkhq haujsyf fggrnbc wsgree rfnppcx key gvdzgfy evdtrrz\r\n"
			+ "oblab wpgm bpyy xuroy qhb adqko\r\n" + "hneb law uzms fhhk yjymdx wjla ixfh yblh\r\n"
			+ "qlvsd bxsq hjaq fuwspzu hyshq idbabc rqcih ilixp wft rglf lmqm\r\n"
			+ "qdskj two ckd qdt hzjvd woo fmmuw\r\n" + "kumc zywzq srafcbb ihfu kfvav\r\n"
			+ "qlkkrq qlkkrq qlkkrq qsc\r\n" + "hob bpecik zqtrfz iqizeu plrer epm zqtrfz xrekeql xrekeql\r\n"
			+ "warszd sxyyorh sxyyorh eztjf warszd kszp\r\n" + "hjbrax liumjue liumjue liumjue\r\n"
			+ "rfnqd folmiu dlicln pdyk uqd rfnqd\r\n"
			+ "mjdu lytfvya xomdujn leaqiyc lgemz lihfnhv zgeml koukz luqda\r\n" + "yqsz zedjmwn aep qwbhd yqsz\r\n"
			+ "etg rmovps abizj yqr kib\r\n" + "yznxec sfqkd ofkzep njr hmeym nsh xdq\r\n"
			+ "ryoyq heoo zuo udvfev ehoo axcnbpu oeho mfenmd shrebzy\r\n" + "uaeh jwllsjp frkhqsy uaeh\r\n"
			+ "giofw hwceb euikqp ldmb kqpkxwv namazcg hqyyzgs cglsqux\r\n" + "qledbd qledbd kbwo wgfmgp\r\n"
			+ "olbsca muxw nxs locsba\r\n" + "gbxxgj xlzm gws pkpwy ofkxb sykhdo nbhrv\r\n"
			+ "najr bfk tbqkm hxabe nvr mdi dmuujr bfil nyripr zcydzy\r\n"
			+ "kiczhcn dfgylw yzkwk nytijj pceu yukj ekaol xpb uep\r\n"
			+ "acyyxn rwczsud acyyxn payiek inusyb rwczsud\r\n"
			+ "mzssokx bshs bshs ocrvlug nzsgvch riejkrd jkj mpmdgsp kvixdfq msmmx\r\n"
			+ "uaxy wpvhf uaaq ranp vfhwp iik kii nvh\r\n" + "shecxef nqpx jly dzm qvmpu kxg hdg\r\n"
			+ "xembm yzevult ljrllc yrlskyk zas wstnz yrlskyk vasra\r\n"
			+ "yoaxppi kzax hvxfezf mek teo cbtlrfa ncxac yee\r\n"
			+ "dzfpbi cynov dje vxypba wcwww cwnu cqtp cnuw wwwcw rkzas\r\n" + "xzwdt jcwv anb xzwdt\r\n"
			+ "fodgjem fmmrsfl eovsneo etzutda paw fmmrsfl jcqql\r\n"
			+ "yfztt alcw nwdmd afgknu njxkj zykz cvv jbnl han iatmruu trqls\r\n"
			+ "yas hpulrmf dzts sltg qsbw fjj rjymnnx dkkv\r\n" + "hwjtgd abmb cfw xoumxn xnoumx cxo xnxmuo alb\r\n"
			+ "hnl zgdiip lrddhl fyw mporhtp waedf dltdfmc lyipoth ubmg hnl\r\n"
			+ "wxard wxard cibp nzquvb muuslvw igvewfh mika wxard\r\n"
			+ "cjqjhva rrhzy qpdc nqnyd enbdee ewrhp cqdp xekgjai\r\n" + "axtmxb axtmxb phl urdqaar urdqaar\r\n"
			+ "umce jult bkart dgdvdwc kqzlzn nqkzlz umlxx cmue xvehqag wxifal\r\n" + "lwsuc ski ubo ksi sik qwcudv\r\n"
			+ "husdv tssr gfp bfzbrp jtmk svvdpb uvshd zbnpdmj svpdvb\r\n"
			+ "nnbvf xbb dobqk xwloqca uxvqti blcwxpu kubwu nognin goywn\r\n" + "xhe dhddftc ggltd dhddftc wspf\r\n"
			+ "jodq cgvnk lpl wkwwlqd prfby bpyfr tbgyqm\r\n"
			+ "bdebxj cuvow jdwdxw kuzh dvxmsyb dyvcxo psf kjnoe odfwgfa\r\n"
			+ "xpfb knzgfsi thmsnbi ymjxn bevohy xpfb\r\n"
			+ "hphcu fjodpdt mfsp jkvvp jvypar nlud lfv uftupcr nul dunl\r\n"
			+ "olz ihyhw qntr lwcbohv qntr wzralwl\r\n" + "kfz pkjhidy msnmwz exox xexo uakipj mmznws zbbji ozispqb\r\n"
			+ "gfi kwdhx qqo kdxwh fig\r\n" + "ehh rfozwr caoisw qntlk pkv zulc kpv hrqz\r\n"
			+ "exmlrj aacc rzb qie rzb\r\n" + "mxyqe cuqz feyd meqyx gdvpu rqyjtvw dmoo vugdp emem\r\n"
			+ "advj xmnad uvh ufnbi xmnad xmnad zzwjksx chbrjas hrbp ruvyg\r\n"
			+ "nasrghk pmol ryko ofgakhd korf vpy nakrsgh\r\n" + "mylyqg aeizp rnk krlwchk aaqg\r\n"
			+ "edxursp sosyv zesgnpx zlo sly alurdc ypmez qib aqtt lmxd\r\n"
			+ "ihm hwzhd jhiw raocjk nlxce yzuzu nhudri tvygl tmclg mdkz\r\n"
			+ "psubdis qrmxebg kdac xvl raxwfx vlx sxme\r\n"
			+ "tci tphdy tggam vqqiyjz sgfvdri sxhztz fhsmxx yaj ncxcxq tic\r\n"
			+ "xkljs cuhrm fdjqwd fuzyzh dzuzgjd lzpye lzpey\r\n"
			+ "jriwl ypkcxd fxrg eit okzzzsc yaykarm qzuv jurgek dzfbbfl\r\n"
			+ "workf rrw absfl gxluw qprdsz absfl qwqbmi amepvz oiqmy workf\r\n"
			+ "dxyyb brnerbx lykd oqmz ursl zqom\r\n" + "cqtuzva aih uhaswd auhwds ktyvc hufogcg\r\n"
			+ "jre fhlgrse svedc prfspaj ghm qcjzfc nsd\r\n" + "fow xyo vlvg sgg jgzvff rjxh eovre xtupnz\r\n"
			+ "pekj pgiecc igxd zbiqoob ovv\r\n" + "xofxmz rdzdiq yruoqkh arfunx yruoqkh ucm bxov\r\n"
			+ "ctogwj lpv ivtoxkf faj ctogwj xfzluad ctogwj vvw\r\n" + "rmc vjxj strgo tykifpp\r\n"
			+ "ulivozu bczond ywnmt shakc yknr psr\r\n"
			+ "bfx alwedh jfomlf pzj tely alwedh vccsoer rgwftcl vccsoer\r\n" + "frkwbv uudwt qsfg onuhiml jrd usu\r\n"
			+ "bgdx deybefo gdj dgbx luu cbuwawd wqqtq dqmwy gin mhtfgy\r\n"
			+ "ohjp ykemg nrs leayrh brtipx jhop phoj\r\n" + "utaep ywsy utaep ywsy\r\n" + "qow dxagjwb qbki bqik\r\n"
			+ "larkpq bdgw mly vvwgv\r\n" + "juar zaerof qekpe hhgd eygru epekq dhgh\r\n"
			+ "xpblz xksc lzue xksc yid nnve trlndn gjczngs cifqoaf\r\n"
			+ "fpv ekz eknldf uqjgeu awwnwxu eknldf eknldf txhxv\r\n"
			+ "mzvk wqtbda ovdbh vnes uiuuc uicuu bpwwtm aaat cygej nio gnl\r\n"
			+ "rkdkzp bjaxqif xuwx bjaxqif hgtz slkqw rkdkzp ztp xfvgk ycvg\r\n"
			+ "zpwr wvxzfcd opgcrfc ytxeboe rcqa ehrga lmgm\r\n" + "brsdnk nqgkjab nbjkaqg gho zqe\r\n"
			+ "szbysu oqrtbp wjpuv oqrtbp oqrtbp gjmqq\r\n" + "uoyi ctscw uoyi ggn ija\r\n"
			+ "fop lxa cgwpw lyvrxbe tit fop fop kfigqnu\r\n" + "ldqmk rxo ajhrbc ahrcjb xqdk kdxq\r\n"
			+ "ith vdrl kvaxktm grkzmon ith ywbz kmnoiz\r\n" + "zdoo omjo fbz dveiipw fbz\r\n"
			+ "ivj mcnu tkijlq xkq lrkyit cumn sfkrk numc ezxeeoi\r\n" + "lcwzdi sbsdgdy olvc olvc bimubzf bimubzf\r\n"
			+ "cdjd umhwh djdc cddj oxheq veazlm\r\n" + "gxszn zsgxn azy yaz\r\n" + "byvmj mjybv jvxkuy akas uxyjvk\r\n"
			+ "whmkttq whgzm gwmzh pkvtljw zgmhw jasudeq\r\n"
			+ "yyjri fxsj xffmna vbal ftff rwq uszym bznil rfuctp ejndv wqr\r\n"
			+ "gnwzjbw dezfvq gzkhzkl ivrdvxx wfah xvivrxd qzdvfe\r\n"
			+ "xnfo zqzn iaod zlcclsd onxf lpskrfk nzqz kqzr kffpwak eky\r\n" + "muc tafbzp nra gvzc xiu gvzc\r\n"
			+ "gfnbnyj nyjbfgn eoosw yjzf\r\n" + "qwwls sqwwl mxph swwql\r\n" + "twor uzjftq twro orwt\r\n"
			+ "qomjuob bqaim zvfqww cvqzm wwipc zsywb bsqkp aoj fus\r\n" + "nlyd gtbgox tajlzgs bgtgxo pqt\r\n"
			+ "pjtmgz ulblj ussh gngagba hhtexq bjbj obe xctciay osriw obe shxri\r\n"
			+ "agc ejjdtak jgq moj agc iua syhxih znavmrc iih qubj\r\n"
			+ "zxwzwhm lipkqhz bbv birxsj gzg iefrjh mprsfs ofpltbl gbo srpmsf hirm\r\n"
			+ "rbpgqoe kymrf uzsut gkbtd xctpg qul hirtfl\r\n"
			+ "wfvg pnqhuv jayjm ftqt mbrotl aydmoc lfwlxk vpvcsi svbn bnsv\r\n"
			+ "jxjxza ysl kls vmt fvgunx hketl oshgie\r\n" + "dfeyxv akx qagwayp qrs lnulrle rqs gbvd bvdg\r\n"
			+ "aac ndptml oke edwrg aac xechxz\r\n" + "mpx yrb oervzb ydvkw avlt oervzb bxdqbo hzwls\r\n"
			+ "dsynfk dsynfk epexzjd epexzjd zofb\r\n" + "vhe zxfolqk lkh fxt flzkxqo lztwkmo khl\r\n"
			+ "izlthi wtokkuz ousbpxp pvr uuxueq lvbeff mfk syjq fwgnfmg yytqesm gdd\r\n"
			+ "kjcg slt khz atzw twpspdx kgyk wgq hjat ntf xvhxol msvdjs\r\n"
			+ "ymm arrggw mmmbvrs ist arrggw nbvvc cwyacp\r\n" + "kuzglex iemp iemp jsko iemp oqs dheqypr\r\n"
			+ "tzztq dsxqbow qgaeo kqn dsxqbow qqzpv\r\n"
			+ "ysr fctpiyn psgb gatavv zsfxoxq nynfoh qaimoj zotjk nxug syr\r\n"
			+ "xvm qvr hdxyhpf cbo xmv lfv wltyjlx\r\n" + "hjq pohc xgqit tducggu zdqmnc xqgit tqxgi srfyzu vdikqx\r\n"
			+ "msiqte ewvp bzrv cmuy gse qqayvb bzrv qehy\r\n" + "watdvu ametrc etlduhh vcc luehdth udavtw\r\n"
			+ "jktj mkq jktj mkq\r\n" + "uekth ufjkmdi qzhge wzwcwk nvrodcc vrcdocn bhcvd\r\n"
			+ "xumywk zwofh kuxmyw acgzsjj hfowz njnz bnklyi\r\n" + "hmm fexu fexu hmm\r\n"
			+ "zeuoarc yoa ggff jazzd mjein yhj qwo qwo\r\n"
			+ "rolkwf fcyat lwm wqqm juwkt wqqm udj tex xgps nyy pdbkkhb\r\n" + "gld ksl gld bnsuhqc gld rwmybj\r\n"
			+ "tvyxk xgmk cri pef epf unsl yktxv\r\n" + "muiql ejq taetjkf ejq xzmo wmv qbtmrh hkfbch taetjkf sut\r\n"
			+ "pqg icvv gpq tufd iixd duft\r\n" + "zekx ybbb gzml vrbwcl opfb fkrv tto cbipr\r\n"
			+ "moh stkkf ynrtdf jlgb kstfk ksktf\r\n" + "nvysvf mdtdoq bqqvr bqqvr\r\n"
			+ "dqyz mzoqtp gzhdgd symsq iwh bpwox\r\n"
			+ "pkqi jgzsrah yfjxx kdp xjaf lbj gkpixnj tyvzzso qmjbo skg nlchzbk\r\n"
			+ "culxfx jarwu eiwriu vwvg gvwv sgnasz\r\n"
			+ "kyfsn dwc sbnoe xwpgjh nbmvec dwc qjdh mpw gefimue fvqjwt kkor\r\n"
			+ "hcdcgxs fof flc hfpjy lii fihcao pxg xywei jwsq yxr\r\n"
			+ "oxrcv pda oxrcv gdvojsz kmlga mixlmp hdcabsn qvoa fwt\r\n"
			+ "poe joylchz humrjy cyxbqfm lyk ybrfmp qmtpqyk vtpr lyk vtpr\r\n"
			+ "ffswqs yxbuj tfzkmc yxbuj giog ckubbfy rtigw rtigw rpitxd\r\n" + "kcvrn eejyftw ejytfew rnckv\r\n"
			+ "lvk lkv cooumh vlk\r\n" + "loypv ukowl loypv nyoyfl vehnm uff\r\n"
			+ "tst sei zovy itdwibj mcbtst wcf rzp xvbtax ffzp xieenuy aegkj\r\n"
			+ "zkhi hvsbgza xbwtdns wypfngy lvabd pybhcd crczm buikdpo vqgon pynfwyg phbcdy\r\n"
			+ "ihy irxrj entmc yxfhbta xsdv xsdv\r\n" + "ezrcv kfgm pjneez puccy gzpxdlf gkfm yucpc mli xezfug\r\n"
			+ "umjppkq idkiri wmnbhi unl nteyw wmnbhi zyv idkiri shhcrau\r\n"
			+ "dzj zveqwae ljnikvb baavr dhsohp zveqwae goq zveqwae\r\n" + "xhc xch bmttdr snd jakd\r\n"
			+ "jmgnvda bdpzfw dfwpzb pimpv blqtbyo lzdzo bgrlfy anmjvdg\r\n"
			+ "lwvu ksg gqbtibd ksg lwvu ohfzlt foajo apyrcwj uaro\r\n" + "vel qksrwp zei ipnvd hdua rkspqw bujf\r\n"
			+ "iozkiu upa knmcug zidypn yswb zswkvx naqsu\r\n" + "tjktoe dqpt pbqi dqpt\r\n"
			+ "lcl tui uoizm xrdpmwi fbsuuqq tgeac hpajm tegac nczlic\r\n"
			+ "ntmm mskzb arem ntmm jayzfe wyurgsh eqwcqt edhska asxhjv jayzfe\r\n"
			+ "jyq juifidx fokzxh cgo xofhzk nhro xyccuq ioa nwk nqaxpfw\r\n"
			+ "cvag bpk cuo ocu buehhq tartafi ifs qwh cveurg\r\n" + "bwut xpfni qzg cmp cid jftawv twiszmo\r\n"
			+ "zgxc sui kypkd vpam ymxicrw jcfbutd fgx jcfbutd\r\n" + "tkxn rjqzljh tkxn mdwcho\r\n"
			+ "qbv zneocv zneocv zneocv\r\n" + "tywf soncr lyepx qzj xdsr pdqv swt\r\n"
			+ "ulu rdk iomqu dgouoba icax\r\n" + "ddsc oxilqpd ddsc atbekg ouzmxf oxilqpd kwtzz yhmyd otvi\r\n"
			+ "vtj llnfrpc vfighju urosrsz vurtse llnfrpc qeuo vfighju nnn smsnp tfom\r\n"
			+ "updfjmz ngtgi zaitq rqqhcyn ladzx zaitq fbaphyz hipe\r\n" + "rii fpos atl tal qhubqdv lat\r\n"
			+ "whxzwdj yznkngr eefbmub wnxitd tnwxid zja ziewilm xylwn ihhsha lrptuyf\r\n"
			+ "fhmzaxv mdn udl gyv pqw qlrz flm rqtji\r\n" + "bgn clnm cnml qyh hhf qqnur sgvigvm\r\n"
			+ "qjtbysc ycbqjts gbgvlz vgzlgb dgxks qbvp grji dcc\r\n"
			+ "wmduuq qayymzo zvh ylbipw sin ybwpli ilypwb\r\n" + "qsvzktt qsvzktt dasmg knh gcgep qai\r\n"
			+ "jxukj qlgr cjssj aavqv\r\n" + "xpxa glsdfxq ngxwon ytuue pizqu\r\n"
			+ "fxl vegoed tct luwm ulwm eeovdg\r\n"
			+ "ntmpe auasx vkwgi cryuiix dmiufo fcb ldl jauncf gyouym asjcryc\r\n"
			+ "lgwdcs eoxm hcrpnuf pcfnhru vlye fpurcnh uquukv vjc\r\n"
			+ "lfns riwpdh phwxvew hhu jfptvv ofxd hkotgfq\r\n" + "qvuwnq wnpvs xdivrfz yaenqr fipwgl\r\n"
			+ "vhcexfd bishqsc gsbruxm yzccyot yjloa aptg vbr gsbruxm ihqhyz yzccyot\r\n"
			+ "knfst zhihi swhhq zhihi\r\n" + "qfto abhjx abhjx bpnijn ogmqxn rclqag dmeb rdogx emfriui hyvp ogmqxn\r\n"
			+ "ivaemm wlsc dvjv aivemm xvf shfonv\r\n"
			+ "vowhosr vptlu ucrut rdynh ttqvhg rdynh abtja pnvdy puxfmf dyhd\r\n"
			+ "uvrenol ycuhvy ygm fjsxiwo oftstid ygm\r\n"
			+ "fix qrqeg dfgvlun fix iraxgtt lhgqdo eqkgshd jwmrm qrsbzba\r\n" + "mxdj icjqzqw fvew gtvlhm mxdj\r\n"
			+ "cyjtkm crb pmg jwo iluc brc ttnd\r\n" + "dasmgp ool ool opc\r\n"
			+ "ubi pmz mtkh ibu hlx ipcvjki sydw zpm eewfdeu oga\r\n" + "avex yjaoghv yjaoghv lwwx\r\n"
			+ "kwkdst iuokd nmpw onayet zlavwnd wwvbr jtrkyku wfxx dumydgh gnd zgi\r\n"
			+ "ahyjnc rjakp bhabq tsmfi ahyjnc tsmfi yitqgi uwnywil shnkbn\r\n"
			+ "krr sbbfjtm yvunas hwppsjf ntuuzw ngyvdmt ynk nfq mfrb pyw hngr\r\n"
			+ "eeecesf phoo ijmx sjp kgmtg sjp wyz\r\n" + "qwixmou oximqwu ixu lsmf\r\n"
			+ "dyrzq lbstdjv ldvowml qjf fqj zpabc dwmvoll jnq\r\n"
			+ "pdtlu hgcfvz mnwjyq ymi cvcp kmx mkx ooffp uiwg opoff uevqt\r\n"
			+ "hflomt fhlmto gutdbyp xyi zpggxc wqe\r\n"
			+ "jpsr wwex yjgdj fqah wrmmw nyrnw hcomcgv teajmu emw zrraid\r\n"
			+ "tvgsca bzgzkga ypsxsk dqz exmu tvgsca dqz qnd\r\n" + "arzn hojpi bznw ejuupe bznw hojpi\r\n"
			+ "rids dule qaefaon sspit mtzgdls cfujw xldhimi igdoy dule\r\n"
			+ "nefsys plea obksngc zxqee avsi obksngc vnsxdrl gspadob avsi owmzpeh tcj\r\n"
			+ "oweq fkr krf rfk ztwjdry shzcmew jhna\r\n" + "hdjizhg dfclic usds luz mcwyj luz qvomls mren otax\r\n"
			+ "pmzzfj pmzzfj wfxyq mqv hyp lhf\r\n" + "dxeaw ckkey ccvawo keaf izlh oacvcw lgcpgeh kdiky\r\n"
			+ "xkwe xekw kwex tzfyx\r\n" + "dmmyt mtdnqw pdw vdav ofrtsk\r\n" + "klz zlk snxnihg snhigxn zkynpd\r\n"
			+ "ijzce xobf uojezxi xiuojez\r\n" + "ztepv zvpet nije aditjlg natkkk dtitg jprgia\r\n"
			+ "fesuh wadrhc bayf kktfaf nxvhq smbdaop gqx ioez fkjufb abyf\r\n"
			+ "hej sta pztkcd pesabzz szp iada iada cdae hej sqst luf\r\n" + "xlnuhn oljaf fljao ascxez fojal\r\n"
			+ "dprclb fzn wgauz rxewtp cjrlgz zfn\r\n" + "fidwoa mvoqy afian ntzokap mkplgy jfukgjv cyfsz\r\n"
			+ "hbvqnnt giinuzq uezugy qooxjc zsxr rnihg ipbels\r\n"
			+ "qroi wtltjq suj tqit bxtc jidzhpe nizp wtltjq nadcdm wwyhjrg\r\n"
			+ "qtr fkbl bpptu baen awjpwsg vvqbxz animt uqbk zvbxvq\r\n" + "nznq fdiul jbv umyrf yufrm hrl duilf\r\n"
			+ "bkvlfuw onkqzeo iwrg rifqzhj mgroul rnor qqqc sbfi hny zosfp kopxb\r\n"
			+ "nvifbx jbowbj fnyskt jbowbj xvun xvun\r\n" + "piyl haajm stwzpp xvjg amjah\r\n"
			+ "gye efwwwiv kyv zmtcgmi ifwvwew\r\n" + "dflx gdtb jyoj jyoj dflx aqhycgi xffnn\r\n"
			+ "inc mpys mzqmcwx vryz ibqrzc pmsy fat rojpxwy rcbqzi gjef";

}
