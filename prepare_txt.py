from glob import glob
import shutil,os
result = list(glob("lrs2_preprocessed/filelists/*"))
print(result)
# result_list = []
# for i,dirpath in enumerate(result):
#     # shutil.move(dirpath,"./data/preprocessed_root/original_data/".format(i))
#     result_list.append("{}".format(i))
# print("\n".join(result_list))

for i in result:
    print(i.split("\\")[1]+'/')

# with open("filelists/train.txt", "a+") as f:
#     f.write(result[i])
#     f.write("/")
#     f.write("\n")