import shutil, glob, re, os.path, sys

pat = re.compile(r'(-\d+)=(.*)')

def backup_file(filename):
    print "Backing up {}".format(filename)
    head, tail = os.path.split(filename)
    dest = os.path.join(head, "Backup of " + tail)
    shutil.copy(filename, dest)

def fix_results(result_dir):
    map_files = glob.glob(os.path.join(result_dir,"*.map"))
    for filename in map_files:
        changed = False
        with open(filename, "rb") as inf:
            lines = inf.readlines()
        for i in xrange(len(lines)):
            line = lines[i].rstrip()
            match = pat.match(line)
            if match:
                num, trans = match.groups()
                numval = long(num)
                numval += 0x100000000
                print "Replacing {} with {} in {}".format(num, numval, filename)
                lines[i] = "{}={}\r\n".format(numval, trans)
                changed = True
        if changed:
            backup_file(filename)
            print "Writing changes to {}".format(filename)
            with open(filename, "wb") as outf:
                for line in lines:
                    outf.write(line)

if __name__ == "__main__" and sys.argv[1]:
    fix_results(sys.argv[1])
