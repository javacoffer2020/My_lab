def level_30() -> None:
    print(f"\033[31mLevel 30\033[0m")
    import re
    import numpy as np
    from PIL import Image

    with open("source/yankeedoodle.csv", "r") as file:
        data = file.read()
    file.close()
    data = re.findall(r"(0.\d*)", data)

    img_data = np.array(data, dtype=np.float).reshape(139, 53)
    im = Image.fromarray(256 * img_data)
    im = im.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT).convert(mode="L")
    im.show()

    info_list = [int(x1[5] + x2[5] + x3[6]) for x1, x2, x3 in zip(data[::3], data[1::3], data[2::3])]
    info = bytes(info_list).decode()
    print(info)


if __name__ == "__main__":
    level_30()

# Level 30
# So, you found the hidden message.
# There is lots of room here for a long message, but we only need very little space to say "look at grandpa", so the rest is just garbage.
# VTZ.l'tf*Om@I"p]#R`cWEBZ40ofSC>OZFkRP0\)+b?Ir)S%Jt3f{ei%n2<FErFx~IzVm JTh =xdx++'de8C5'|>2\/We;ib(b%d$N<2u(o$*d@.*6Fd'nW5#J!}a]T"1Q-7Y~bOF]T+^9d]e^J^=&I&<x|EEgdQ$$pX'f!_n>F0([j%Y'XjwWu,4w/q;1Hd#1H{{Nf~BQ6f![m#fb^a;{Ei%$2fEyN[*4KhK[-7({jh5k0n kwZyx|x=xvFCfU}n`Y'|}x(^pQ.(1`!Z'ns>LL=9yZXl["@:{fWKvOq0B+ShQ4,-BwWJSB|cedVq}AWzn=X.EYfe;PsBt>r)vboMvai75tARu;A*7?2bJ0uEhoH.o0xp7QV>[Xw*H|m^(n>4X<ex!PQU<f+"NKAo~nH=v6|hcS-$Hu=m|A &]q(w3h6r=X@mu85aT4 KLO%VRGNjK8W<.eUhWEHXE7$?HB\ge+dp:&I]^y[:}!]QP>4y~/M\*w#'pb-ju\BX=J>L@H?m[ih[@_>I*QsO)LL;mw=Do3"bJ=mk:0*TUd'<czm\8IN%6cM|n6^,s] F(JG=+2>78KMW^!W+!?-)U-R+ROWY3^r0uG.qMLX1x[aL+&.z8X}}_Uhl,%Y"Vt_]yec z1=7Hlk&yg8505BTl14MREiZBg_i 8(\qAa9zPt@!JbJG<G+{@e<H>f%LKlU'VbbT{P?Px'+=g}UsW;"oomK\N]DZi8e8be6l*ICAjk~r2:qDI!?%#pNKW{(j[trOA=2hxx%@TIGCPP*JcNi<qmpv3{uB%(\c!y4>$@C=^Hjp>)*]v&yr-8BRpm~RbmlfkV|B/F:ykxd.za#@&_AVz$Sy_%g\/Y|2"p/{U4ed L|!#=g+aeSQ{n*CkRoU(QhM "rXGsQe#!`,"grX)AKkwHua3JTi_|r9lm?AEx;A_W8nr,(7Y*YVFgtVwvl_a+CmO3nacFnO`9lxlUZit\H6A*L2]M#N.0@?Cje6hBfEF^osiKR>L?^1zqaO]{gs6|jh`$+i#1'B%WQf(.p$EXT%Fs"RPi~[;bfEI-0|+(kqz;9K}buyqOpl/nw^`6>:R0MI|a(uE&K"z@!k:9o)LCb!)B!0#ze\hRx1):?%Z=H(+9c4(vGesP;wpt`V^cP>o)r&&4AZF"a{E?CE)Mc"(<@2Ez{)"%R6b5]dl0.\s3U4:ec:,OT<i^nAslj}79O2mJ8G,:P>gaIDoDjpen'IC*fZ{:^.r=.tSjH=pnii"q*hxOD|Rxk-x)?Z/weo (^3JAs&S=:}KsDKnnA7"@V/#I|3CX<>~?hNoT"v?=y9bC\9^7zI0I!CmZR,3P"F7-_'slm3}oV<cRJ*1uVyr|1F[v"vc,3/A\2v3s3e76eG+8#`9q!H2pr6|0hNO.Pxw*eee)q,tAF>v;M/D0((m[%>(D}YQ^Z7{@S''8ltU"Cy/(Kbha;?8$@~rv(H7xw,sD+7"+If!['^j{z":hw4cS"m+p50"5,/GLahJXr=WP#?:/l|C-!42EBXvl/pQZ_=WhsAs*F6_S'1.-zgR\;4nMaE<x)\MdB4#o]64I]'>o"QW INlLw1?A."QN<]_oc]Vi?~u,p3?02AZ'c\c$qvh 6sO"hDO.WV7t%VQ~bw~E(O0oe$LS9`Ofkt{*D?~tA$CB@x|F(5v0KJnUq#8W.']'SC0j7qUB~(tn#%RiQ:livgDA?fLRI^SHaE!Rx!j8X3HI<*N%3[Sm$6$)O[6|0s1QoJp\_zM]i91.[1|EcL)RhnWy+WOEi%Ue=N~{L-ZR|9{Fd(u+6o&b2f')tfqcp}PT?M*z=7fqZR|Xn!K1z.bM_AEz>_>ii54G4%h%Aq8)* bi5N{!{ocF'^cMw }'9NI`KR+(__uq 4KKUvkt|x+Ve}v7,H0o`:RCgV2 P#[M<^q+q=fJKarxU?~^^O<Gg-n\Roj)a+<,+.Klhqj`71FVK'olF4AI0=gj^NYKauZisS@ARQ9U"}IYu2VQRaw{>gQzGci 8gx<Bv!Y6criKBUAz5bBKjm<u^B\{SC6bV'6RtZj,YSAekt>m>w44AF/O1;nKBG3:az&//GT;nz-`d%zjqGD2F=*A@<,Q5mk5/u{JuRyUSJ1y,z9]-."f$~rDVhH!m(:A'Z`l~Cy ]I,Mo.eGI"nW/4c<O8S8TXfLAr($/uzE(dtr"v^:K/f@O>8r.5yOQ^wik.18;H&Fe-F{&S_z6P`q}p(!JAaikD~V}7!1MVvwB"-=.U-BLFbaMMpK3bo_OT
