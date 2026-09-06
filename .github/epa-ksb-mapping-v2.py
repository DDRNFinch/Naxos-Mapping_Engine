import json
from pathlib import Path

P=Path('assessment-plans.json')
data=json.loads(P.read_text(encoding='utf-8'))
M='multiple-choice-test'; R='practical-assessment-with-questions'; I='interview-underpinned-by-portfolio'
labels={M:'Multiple-choice test',R:'Practical assessment with questions',I:'Interview underpinned by a portfolio of evidence'}

def add(target,prefix,nums,method):
    for n in nums: target[f'{prefix}{n}']=method

def ordered(mapping):
    return dict(sorted(mapping.items(),key=lambda kv:(kv[0][0],int(kv[0][1:]))))

def finish(course,mapping,title,url,version):
    course['methodLabels']=labels
    course['ksbMethods']=ordered(mapping)
    course['portfolioKsbs']=[k for k,v in ordered(mapping).items() if v==I]
    course['mappingSource']={'title':title,'url':url,'version':version}

brick={}
add(brick,'K',[1,3,5,6,7,8,9,11,14,15,18,19],M); add(brick,'K',[2,10,12,13,17,21,22,23,29],R); add(brick,'K',[4,16,20,24,25,26,27,28,30,31],I)
add(brick,'S',[1,2,4,5,6,7,8,9,10,11,12,15],R); add(brick,'S',[3,13,14,16,17,18,19,20,21,22],I)
add(brick,'B',[1,3],R); add(brick,'B',[2,4,5,6],I)
finish(data['courses']['ST0095'],brick,'Skills England · Bricklayer ST0095 v1.2 KSB mapping table','https://skillsengland.education.gov.uk/apprenticeships/st0095-v1-2?view=epa','1.2')

core={}
add(core,'K',[1,3,5,6,9,10,11,14,17,40],M); add(core,'K',[2,8,12,15],R); add(core,'K',[4,7,13,16,18,19,20],I)
add(core,'S',[1,2,5,6,7,9,10,11],R); add(core,'S',[3,4,8,12,13],I)
core.update({'B1':R,'B2':I,'B3':I,'B4':I,'B5':I})
site=dict(core)
add(site,'K',[21,22,23,25],R); add(site,'K',[26],M); add(site,'K',[24,27,28,29],I)
add(site,'S',[15,16,18,20,21],R); add(site,'S',[14,17,19,22],I)
finish(data['courses']['ST0264-SITE'],site,'Skills England · Carpentry and joinery ST0264 v1.4 KSB mapping table · Site Carpenter','https://skillsengland.education.gov.uk/apprenticeships/st0264-v1-4?option=Site+Carpenter&view=epa','1.4')

aj=dict(core)
add(aj,'K',[30,31,38],M); add(aj,'K',[32,34],R); add(aj,'K',[33,35,36,37,39],I)
add(aj,'S',[23,26,30],R); add(aj,'S',[24,25,27,28,29],I)
finish(data['courses']['ST0264-AJ'],aj,'Skills England · Carpentry and joinery ST0264 v1.4 KSB mapping table · Architectural Joiner','https://skillsengland.education.gov.uk/apprenticeships/st0264-v1-4?option=Architectural+Joiner&view=epa','1.4')

pmo={}
add(pmo,'K',[1,2,3,8,12,14,19,20,21,22,26,30],M); add(pmo,'K',[6,7,10,15,16,17,23],R); add(pmo,'K',[4,5,9,11,13,18,24,25,27,28,29,31],I)
add(pmo,'S',[1,2,6,7,8,10,13,14,15,16,19],R); add(pmo,'S',[3,4,5,9,11,12,17,18,20,21,22,23,24,25],I)
pmo.update({'B1':I,'B2':I,'B3':R,'B4':I,'B5':I,'B6':I})
finish(data['courses']['ST0171'],pmo,'Skills England · Property Maintenance Operative ST0171 v1.1 KSB mapping table','https://skillsengland.education.gov.uk/apprenticeships/st0171-v1-1?view=epa','1.1')

data['schemaVersion']=2
P.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
