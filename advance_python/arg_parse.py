import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--name", help="Please enter your name")
    parser.add_argument("--age", help="Please enter your age")
    
    args = parser.parse_args()

    print(args.name)
    print(args.age)