import os
langs = ['php']
for lang in langs:
    for filename in os.listdir('./resources/'+lang):
        with open(os.path.join('./resources/'+lang, filename), 'r') as f:
            buff = f.readlines()
        for i in range(len(buff)):
            if not ("#include" in buff[i] or "import" in buff[i] or '<?' in buff[i]) or '</applet>' in buff[i]:
                del buff[i]
            else:
                break
        with open(os.path.join('./resources/'+lang, filename), 'w') as f:
            f.writelines(buff)
        print(f"file processed{filename}")
