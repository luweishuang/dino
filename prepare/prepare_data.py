import json
import os


base_dir = '/data/others/competition2021/cvpr2021_SKU'
with open(os.path.join(base_dir, 'val.json'), 'r') as fr:
    content = fr.read()
    src_data = json.loads(content)

data_dict = {}
for cur_i in src_data["images"]:
    class_id = cur_i["class_id"]
    image_id = cur_i["image_id"]
    if class_id not in data_dict:
        data_dict[class_id] = [image_id]
    else:
        data_dict[class_id].append(image_id)

all_dir = os.path.join(base_dir, 'data')
val_dir = os.path.join(base_dir, 'val')
os.makedirs(val_dir, exist_ok=True)
for cur_sub in os.listdir(all_dir):
    sub_path = os.path.join(all_dir, cur_sub)
    # if len(os.listdir(sub_path)) != len(data_dict[cur_sub]):
    #     print("cur sub_folder is not equal--->", cur_sub)
    #     print(len(os.listdir(sub_path)), len(data_dict[cur_sub]))
    #     print(data_dict[cur_sub])
    #     continue
    if cur_sub in data_dict:
        val_sub_path = os.path.join(val_dir, cur_sub)
        os.makedirs(val_sub_path, exist_ok=True)
    else:
        print("cur sub not in dict--->", cur_sub)
    for cur_f in os.listdir(sub_path):
        if cur_f in data_dict[cur_sub]:
            cur_img_path = os.path.join(sub_path, cur_f)
            cur_train_img_path = os.path.join(val_sub_path, cur_f)
            os.system("mv %s %s" % (cur_img_path, cur_train_img_path))
        else:
            print("cur img not in dict--->", cur_sub, ", ", cur_f)



