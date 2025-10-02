# Take subject marks as command line arguments
# example: 
#     python3 cmd.py --physics 60 --chemistry 70 --maths 90
# Find average marks for the three subjects using command line input of marks.

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--physics", type=int, required=True, help="Physics marks")
    parser.add_argument("--chemistry", type=int, required=True, help="Chemistry marks")
    parser.add_argument("--maths", type=int, required=True, help="Maths marks")

    args = parser.parse_args()
    
    physics = (args.physics)
    chemistry = args.chemistry
    maths = args.maths
    
    avg = (physics + chemistry + maths)/3
    
    print(f"Physics: {physics}, Chemistry: {chemistry}, Maths: {maths}")
    print(f"Average Marks = {avg}")