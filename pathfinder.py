from PIL import ImageColor

def get_data(file):
    data =[]
    with (open(file,"r",encoding='utf8')) as f:
        lines=f.readlines()
        for i in range(len(lines)):
            data.append(lines[i].split())
            return data
        
        data = get_data()
        print(type(data),len(data),len(data[0]))



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='pathfinder stuff')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        data = get_data(file)
        print(data)
    else:
        print(f"{file} does not exist!")
     
