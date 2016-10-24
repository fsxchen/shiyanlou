from github3 import login



passwd = raw_input("please input password:")
gh = login('fsxchen@gmail.com', password=passwd)


def create_repo(name):
    print dir(gh)
    try:
        r = gh.create_repository(name)
    except Exception, e:
        pass
    repo = gh.repository("fsxchen", name)
    print dir(repo)
    print "======================"
    print repo.url



if __name__ == "__main__":
    import sys
    repo_name = sys.argv[1]
    create_repo(repo_name)
