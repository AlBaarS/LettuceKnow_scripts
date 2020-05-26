import pandas as pd

# This script was made to further sort the InterPro data provided by Joël Klein (WU). The data was already sorted on
# signal peptides, transmembrane domains and the absence/presence of a kinase domain. I looked up the domains that can
# occur in plant RLPs/RLKs in literature, searched the respective annotation at
# https://www.ebi.ac.uk/interpro/entry/InterPro/?search=#table and searched for them in the sorted csv with InterPro
# data.

# data prep
ykin_csv = open("F:\Afstuderen\data\interpro_SP_TM_Kin.csv")
nkin_csv = open("F:\Afstuderen\data\interpro_SP_TM_no-Kin.csv")

# empty lists
LRR_lst = []
LysM_lst = []
L_lec_lst = []
G_lec_lst = []
B_lec_lst = []
C_lec_lst = []
Mal_L_lst = []
GNK2h_lst = []
Thaum_lst = []
Chiti_lst = []
EGF_R_lst = []
ProRi_lst = []
PAN_lst = []
TNFR_lst = []
hitlist = [LRR_lst,LysM_lst,L_lec_lst,G_lec_lst,B_lec_lst,C_lec_lst,Mal_L_lst,GNK2h_lst,Thaum_lst,Chiti_lst,EGF_R_lst,ProRi_lst,PAN_lst,TNFR_lst]

annot_lst = []

# domains
LRR = ['LRR']
LysM = ['PTHR20932:SF36','PTHR20932:SF38','PTHR20932','PTHR33734:SF11','PTHR33734:SF13','PTHR33734:SF16','PTHR33734','PTHR45927:SF11','PTHR45927','PTHR46204:SF10','PTHR46204','PF01476','PF04225','PS51782','SM00257','SM00584']
L_lectin = ['L-lectin','PTHR27007:SF140','PTHR27007:SF145','PTHR27007:SF161','PTHR27007:SF162','PTHR27007:SF166','PTHR27007:SF170','PTHR27007:SF175','PTHR27007:SF180','PTHR27007:SF187','PTHR27007:SF188','PTHR27007:SF192','PTHR27007:SF193','PTHR27007:SF195','PTHR27007:SF202','PTHR27007:SF207','PTHR27007:SF21','PTHR27007:SF212','PTHR27007:SF218','PTHR27007:SF223','PTHR27007:SF231','PTHR27007:SF237','PTHR27007:SF241','PTHR27007:SF243','PTHR27007:SF251','PTHR27007:SF252','PTHR27007:SF253','PTHR27007:SF257','PTHR27007:SF262','PTHR27007:SF265','PTHR27007:SF272','PTHR27007:SF273','PTHR27007:SF275','PTHR27007:SF282','PTHR27007:SF75','PTHR27007','PS51328','PF00139','PS00307','PS00308']
G_lectin = ['PTHR27002:SF467','PTHR27002:SF555','PTHR27002:SF577','PTHR27002:SF591','PTHR27002:SF685','PTHR27002:SF694','PTHR27002:SF701','PTHR27002:SF747','PTHR27002:SF749','PTHR27002:SF789','PS50927','PF01453','SM00108']
B_lectin = ['B-lectin','PTHR33793:SF2','PTHR33793','PF05792','PF07468','PF11766','PF18021','SM01056']
C_lectin = ['PTHR10334:SF245','PTHR14789:SF5','PTHR14789','PTHR21407:SF5','PTHR21407','PTHR22799:SF1','PTHR22799:SF2','PTHR22799','PTHR22800','PTHR22802','PTHR22802:SF10','PTHR22802:SF11','PTHR22802:SF14','PTHR22802:SF194','PTHR22802:SF220','PTHR22802:SF221','PTHR22802:SF226','PTHR22802:SF237','PTHR22802:SF238','PTHR22802:SF240','PTHR22802:SF245','PTHR22802:SF247','PTHR22802:SF249','PTHR22802:SF261','PTHR22802:SF266','PTHR22802:SF267','PTHR22802:SF323','PTHR22802:SF341','PTHR22802:SF344','PTHR22802:SF346','PTHR22802:SF349','PTHR22802:SF362','PTHR22802:SF364','PTHR22802:SF366','PTHR22802:SF367','PTHR22802:SF371','PTHR22802:SF375','PTHR22802:SF383','PTHR22803:SF113','PTHR22803:SF125','PTHR22803:SF126','PTHR22803','PTHR22991:SF40','PTHR22991:SF41','PTHR22991:SF42','PTHR22991','PTHR23062:SF2','PTHR23062:SF3','PTHR23062:SF4','PTHR23062:SF6','PTHR23062:SF7','PTHR23062','PTHR23124:SF129','PTHR23124:SF130','PTHR23124:SF132','PTHR23124:SF133','PTHR23124:SF134','PTHR23124:SF135','PTHR23124:SF136','PTHR23124:SF137','PTHR23124:SF138','PTHR23124:SF44','PTHR23124:SF50','PTHR23124:SF74','PTHR23124','PTHR24033:SF181','PTHR24033','PTHR31024:SF11','PTHR31024:SF2','PTHR31024:SF3','PTHR31024:SF5','PTHR31024:SF6','PTHR31024:SF7','PTHR31024:SF8','PTHR31024:SF9','PTHR31024','PTHR45710:SF10','PTHR45710:SF12','PTHR45710:SF2','PTHR45710:SF3','PTHR45710:SF4','PTHR45710:SF5','PTHR45710:SF8','PTHR45710','PTHR45784:SF3','PTHR45784','PTHR46490:SF1','PTHR46490:SF2','PTHR46490:SF4','PTHR46490','PTHR46746:SF4','PTHR46746','PTHR47218:SF1','PTHR47218','PTHR47498:SF1','PTHR47498','PTHR47517:SF1','PTHR47517:SF2','PTHR47517:SF3','PTHR47517','PTHR47536','PTHR47536:SF1','PTHR47629:SF1','PTHR47629:SF3','PTHR47629:SF4','PTHR47629:SF5','PTHR47629:SF6','PTHR47629:SF7','PTHR47629:SF9','PTHR47629','PTHR47647','PTHR47647:SF1','PTHR47727','PTHR47727:SF1','PTHR47753:SF1','PTHR47753:SF2','PTHR47753:SF3','PTHR47753','PTHR47761:SF1','PTHR47761:SF2','PTHR47761:SF3','PTHR47761:SF4','PTHR47761','PF05473','PF07979','PF16825','PS50041','PS00615','SM00034']
Malectin_like = ['PF12819']
GNK2_homolog = ['PF01657','PS51473']
Thaumatin = ['PTHR31013','PTHR31013:SF10','PTHR31013:SF11','PTHR31013:SF2','PF00314','PS51367','PS00316','SM00205']
Chitinase = ['PTHR11177','PTHR11177:SF140','PTHR11177:SF144','PTHR11177:SF147','PTHR11177:SF202','PTHR11177:SF235','PTHR11177:SF317','PTHR11177:SF324','PTHR11177:SF332','PTHR11177:SF334','PTHR11177:SF338','PTHR11177:SF340','PTHR11177:SF342','PTHR11177:SF344','PTHR11177:SF345','PTHR11177:SF346','PTHR11177:SF351','PTHR11177:SF354','PTHR11177:SF82','PTHR22595','PTHR22595:SF111','PTHR22595:SF131','PTHR22595:SF133','PTHR22595:SF136','PTHR22595:SF137','PTHR22595:SF139','PTHR22595:SF37','PTHR22595:SF96','PTHR33825:SF14','PTHR33825','PTHR42976:SF1','PTHR42976','PTHR46066:SF1','PTHR46066:SF2','PTHR46066','PTHR46073:SF1','PTHR46073:SF3','PTHR46073:SF4','PTHR46073:SF5','PTHR46073:SF6','PTHR46073:SF7','PTHR46073:SF8','PTHR46073','PF00182','PF06483','PF08329','PF16141','PF18683','PS00773','PS00774']
EGF_repeats = ['PTHR10574:SF287','PTHR10574:SF298','PTHR10574','PTHR24035','PTHR24035:SF106','PTHR24035:SF127','PTHR24035:SF130','PF18372','SM00181']
Proline_rich = ['PTHR27001:SF36','PTHR27001:SF489','PTHR27001:SF616','PTHR27001:SF626','PTHR27001:SF636','PTHR27001:SF662','PTHR27001:SF685','PTHR27001:SF729','PTHR27001:SF792','PTHR27001:SF819','PTHR27001:SF822','PTHR27001:SF840','PTHR27001:SF845','PTHR27001:SF89','PTHR31852:SF130','PTHR35718:SF2','PTHR23201','PF02095','PF04554','PF06904']
PAN = ['PF00024','PF14295']
TNFR = ['PF00020','PF12191','PS50050']
domains = [LRR,LysM,L_lectin,G_lectin,B_lectin,C_lectin,Malectin_like,GNK2_homolog,Thaumatin,Chitinase,EGF_repeats,Proline_rich,PAN,TNFR]

# filter domains from file with kinases
for line in ykin_csv:
    tmp = line.split(",")
    for m in tmp:
        for x in range(0,14):
            for n in domains[x]:
                if n in m:
                    hitlist[x].append(line)
                    annot_lst.append(m)

# filter domains from file without kinases
for line in nkin_csv:
    tmp = line.split(",")
    for m in tmp:
        #print(m)
        for x in range(0,14):
            for n in domains[x]:
                if n in m:
                    hitlist[x].append(line)
                    annot_lst.append(m)

# count hits per domain
for lst in hitlist:
    tmp = set(lst)
    lst = list(tmp)
    print(len(lst))
tmp = set(annot_lst)
annot_lst = list(tmp)
annot_lst.sort()
print('Annotations that hit:',str(len(annot_lst)))

# now we are going to determine which hits belong to which line and store that in a list
out_lst = []
for x in range(0,14):
    for line in hitlist[x]:
        tmp = line.split(',')
        lst = []
        for y in 0,4:
            lst.append(tmp[y])
        for n in annot_lst:
            if n in tmp:
                lst.append(n)
        if lst not in out_lst:
            out_lst.append(lst)
print('Total RLPs/RLKs as estimated by domain searching:', str(len(out_lst)))
# now let's write that to a file
out = open('F:\Afstuderen\data\hits_and_annotation.txt','w')
for elem in out_lst:
    for n in elem:
        out.write(n + '\t')
    out.write('\n')
out.close()

# and finally, write each protein ID to a file with their domains
out_rlk = open('F:\Afstuderen\data\hits_and_domain_rlk.txt','w')
out_rlp = open('F:\Afstuderen\data\hits_and_domain_rlp.txt','w')
out_IDs = open('F:\Afstuderen\data\protID_rlp_rlk.txt','w')
out_lst_rlk = []
out_lst_rlp = []
dom_names = ['LRR','LysM','L-type lectin','G-type lectin','B-type lectin','C-type lectin','Malectin-like domain','GNK2_homologous domain','Thaumatin','Chitinase','EGF-repeats','Proline-rich domain','PAN domain','TNFR']
for m in out_lst:
    tmp = []
    for x in range(0,14):
        for n in domains[x]:
            if 'kin' in m:
                kin = True
                if n in m:
                    tmp.append(dom_names[x])
            elif 'kin' not in m:
                kin = False
                if n in m:
                    tmp.append(dom_names[x])
    tmps = set(tmp)
    tmp = list(tmps)
    tmp.insert(0,m[0])
    if kin == True:
        out_lst_rlk.append(tmp)
    elif kin != True:
        out_lst_rlp.append(tmp)

print('Total amount of RLKs:', str(len(out_lst_rlk)))
print('Total amount of RLPs:', str(len(out_lst_rlp)))

for elem in out_lst_rlk:
    out_IDs.write(elem[0] + '\n')
    for n in elem:
        out_rlk.write(n + '\t')
    out_rlk.write('\n')
out_rlk.close()

for elem in out_lst_rlp:
    out_IDs.write(elem[0] + '\n')
    for n in elem:
        out_rlp.write(n + '\t')
    out_rlp.write('\n')
out_rlp.close()
out_IDs.close()