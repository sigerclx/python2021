class Tree(object):
    def __init__(self, data):
        self.data = data
        self.root_node = list()
        self.common_node = dict()
        self.tree = list()

    def find_root_node(self) -> list:
        """
        查找根节点
        :return:根节点列表
        """
        # self.root_node = list(filter(lambda x: x["father_id"] is None, data))
        for node in self.data:
            # 假定father_id是None就是根节点
            #例如有些数据库设计会直接把根节点标识出来
            if node["father_id"] is None:
                self.root_node.append(node)
        return self.root_node

    def find_common_node(self) -> dict:
        """
        寻找共同的父节点
        :return: 共同的父节点字典
        """

        for node in self.data:
            father_id = node.get("father_id")
            # 排除根节点情况
            if father_id is not None:
                # 如果父节点ID不在字典中则添加到字典中
                if father_id not in self.common_node:
                    self.common_node[father_id] = list()
                self.common_node[father_id].append(node)
        return self.common_node

    def build_tree(self, ) -> list:
        """
        生成目录树
        :return:
        """
        self.find_root_node()
        self.find_common_node()
        for root in self.root_node:
            # 生成字典
            base = dict(name=root["name"], id=root["id"], child=list())
            # 遍历查询子节点
            self.find_child(base["id"], base["child"])
            # 添加到列表
            self.tree.append(base)
        return self.tree

    def find_child(self, father_id: int, child_node: list):
        """
        查找子节点
        :param father_id:父级ID
        :param child_node: 父级孩子节点
        :return:
        """
        # 获取共同父节点字典的子节点数据
        child_list = self.common_node.get(father_id, [])
        for item in child_list:
            # 生成字典
            base = dict(name=item["name"], id=item["id"], child=list())
            # 遍历查询子节点
            self.find_child(item["id"], base["child"])
            # 添加到列表
            child_node.append(base)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = [
        {"id": 1, "father_id": None, "name": "01"},
        {"id": 2, "father_id": 1, "name": "0101"},
        {"id": 3, "father_id": 1, "name": "0102"},
        {"id": 4, "father_id": 1, "name": "0103"},
        {"id": 5, "father_id": 2, "name": "010101"},
        {"id": 6, "father_id": 2, "name": "010102"},
        {"id": 7, "father_id": 2, "name": "010103"},
        {"id": 8, "father_id": 3, "name": "010201"},
        {"id": 9, "father_id": 4, "name": "010301"},
        {"id": 10, "father_id": 9, "name": "01030101"},
        {"id": 11, "father_id": 9, "name": "01030102"},
    ]
    new_tree = Tree(data=data)

    print(new_tree.build_tree())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
