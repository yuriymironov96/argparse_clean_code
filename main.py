from src.args import Args


if __name__ == "__main__":
    args = Args("l,p#,d*", ["l=true", "p=8080", "d=/usr/logs"])
    print(args.get_boolean("l"))
    print(args.get_int("p"))
    print(args.get_string("d"))
