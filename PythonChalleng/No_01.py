# str_old = [chr(i) for i in range(97,123)]
# str_new = [chr(i) for i in range(99,123)]
# str_new += ['a', 'b']
# transdict = dict(zip(str_old, str_new))
# transtable = str.maketrans(''.join(str_old), ''.join(str_new))
#
#
# def transword(chr, transdict):
#     return transdict.get(chr, chr)
#
#
# txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# txt_new = ''
# for chr in txt:
#     txt_new += transword(chr, transdict)
#
# print(txt_new)
#
# txt1 = 'map'
# print(txt1.translate(transtable))

transtab = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
print(
    "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".translate(
        transtab))
print('map'.translate(transtab))
