import json
import argparse
import logging
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser(description='Extract target class')
    parser.add_argument(
        '--input',
        dest='inp',
        help='input json file',
        required=True,
        type=str
    )
    parser.add_argument(
        '--output',
        dest='out',
        help='output json file',
        required=True,
        type=str
    )
    parser.add_argument('--t', nargs='+', help='target classes', required=True, type=int)
    parser.add_argument('--r', nargs='+', help='renamed id for classes', required=True, type=int)
    parser.add_argument('--rs', nargs='+', help='renamed str for classes', required=True)

    return parser.parse_args()

def main(args):
    print('Processing {} -> {}'.format(args.inp, args.out))
    in_fp = open(args.inp,"r")#read original json file as in_fp
    json_in = json.load(in_fp)
    target = args.t
    rename = args.r
    rename_str = args.rs
    if len(target) != len(rename) or len(rename) != len(rename_str):
        raise ValueError("target size must equal to rename")
    annos = json_in["annotations"]
    images = json_in["images"]
    newimages = []
    image_ids = []
    newannos = []
    print('Processing annotations')
    for i in tqdm(range(len(annos))):
        ann = annos[i]
        if ann['category_id'] in target:
            newann = ann
            newann['category_id'] = rename[target.index(ann['category_id'])]
            newannos.append(newann)
            if ann['image_id'] not in image_ids:
                image_ids.append(ann['image_id'])
    
    print('Processing images')
    for i in tqdm(range(len(images))):
        image = images[i]
        if image['id'] in image_ids:
            newimages.append(image)

    print('Processing categories')
    newcats = []
    for cid in target:
        newid = rename[target.index(cid)]
        newstr = rename_str[target.index(cid)]
        id_str = {}
        id_str['id'] = newid
        id_str['name'] = newstr
        if id_str not in newcats:
            newcats.append(id_str)
 
    result = {}
    result["images"] = newimages
    result["annotations"] = newannos
    result["info"] = json_in["info"]
    result["licenses"] = json_in["licenses"]
    result['categories'] = newcats
    fq = open(args.out,"w")
    json.dump(result,fq)
    logging.info('Processing done')

if __name__ == "__main__":
    args = parse_args()
    main(args)
