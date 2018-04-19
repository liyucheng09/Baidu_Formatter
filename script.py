import json
import pprint

true=True
false=False
question_id=0

all_files=[
	#.....
]

source_path=''
output_path=''

for f in all_files:
	file1=open(path+f,'r',encoding='utf-8')
	l=file1.readlines()
	data=[]
	for i in l:
		data.append(eval(i))
	file1.close()
	result={}
	result['data']=[]
	result['version']='1.0'

	for i in data:
		re={}
		re['title']=i['question']
		re['paragraphs']=[]
		count=0
		lim=len(i['answers'])
		for a in i['documents']:
			if(a['is_selected'] and count<lim):
				add={}
				add['context']=''.join(a['paragraphs'])
				if(i['answers'][count] in add['context']):
					start=add['context'].find(i['answers'][count])
				else:
					start=-1
				add['qas']=[{
					'answsers':[
						{
							'answer_start':start,
							'text':i['answers'][count]
						}
					],
					'question':a['title'],
					'id':question_id
				}]
				question_id+=1
				count+=1
				re['paragraphs'].append(add)
		result['data'].append(re)
		
	file2=open(path+f,'w',encoding='utf-8')
	r=json.dumps(result,ensure_ascii=False)
	file2.write(r)
	file2.close()
	print(f,'   ok!!!')