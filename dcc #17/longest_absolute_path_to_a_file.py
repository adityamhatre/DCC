class File:
    def __init__(self, inode, name, level):
        self.inode = inode
        self.name = name
        self.level = level

    def __repr__(self):
        return "{}\t{}\t{}".format(self.inode, self.name, self.level)


class FileSystem:
    def __init__(self):
        self.files = []

    def add(self, file_obj):
        self.files.append(file_obj)


fs = "dir\n\tsubdir1\n\t\tsubsubdir1\n\t\tfile1.ext\n\t\tfile2.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tsubsubsubdir1\n" \
     "\t\t\tfile2.ext\n\t\t\tsubsubsubdir2\n\tfile3.ext"
# fs = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tf3.ext"
# print(fs)
# print("\n\n")
nodes = fs.split("\n")
file_system = FileSystem()
for i, node in enumerate(nodes):
    _inode = i
    _name = node.replace("\t", "")
    _level = node.count("\t")
    _file = File(_inode, _name, _level)
    file_system.add(_file)

# for f in file_system.files:
#     print(f)

child_parent_map = {}


def parent_of(inode, level):
    if inode in child_parent_map:
        if not child_parent_map[inode] == 0:
            parent_of(child_parent_map[inode], level - 1)
            return
    i = inode - 1
    while i >= 0:
        if file_system.files[i].level == level - 1:
            child_parent_map[inode] = i
            if not file_system.files[i].level == 0:
                parent_of(file_system.files[i].inode, level - 1)
                return
        i -= 1


for f in reversed(file_system.files):
    if f.name.__contains__("."):
        parent_of(f.inode, f.level)


def get_path_length(inode):
    len_until_now = len(file_system.files[inode].name)
    p = child_parent_map[inode]
    if p == 0:
        return len_until_now + len(file_system.files[p].name) + file_system.files[inode].level
    while p != 0:
        len_until_now += len(file_system.files[p].name)
        p = child_parent_map[p]
    return len_until_now + len(file_system.files[0].name) + file_system.files[inode].level


max_len = -1
for f in file_system.files:
    if f.name.__contains__("."):
        path_length = get_path_length(f.inode)
        if path_length > max_len:
            max_len = path_length
print(max_len)
