import os

# 全局变量：用列表存多个学生字典
student_list = []
filename = "score.txt"


def load_data():
    """从文件读取学生数据，文件读写 + 异常处理"""
    global student_list
    student_list = []
    if not os.path.exists(filename):
        return
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # 格式：学号,姓名,成绩
                stu_id, name, score = line.split(",")
                student_dict = {
                    "id": stu_id,
                    "name": name,
                    "score": float(score)
                }
                student_list.append(student_dict)
    except Exception as e:
        print(f"读取文件出错：{e}")


def save_data():
    """保存学生数据到文件"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for stu in student_list:
                line = f"{stu['id']},{stu['name']},{stu['score']}\n"
                f.write(line)
        print("✅ 数据保存成功！")
    except Exception as e:
        print(f"保存文件出错：{e}")


def add_student():
    """添加学生"""
    print("----- 添加学生 -----")
    stu_id = input("请输入学号：")
    # 判断学号是否重复
    for stu in student_list:
        if stu["id"] == stu_id:
            print("❌ 该学号已存在！")
            return
    name = input("请输入姓名：")
    # 异常处理：成绩必须是数字
    try:
        score = float(input("请输入成绩："))
    except ValueError:
        print("❌ 成绩必须输入数字！")
        return
    new_stu = {"id": stu_id, "name": name, "score": score}
    student_list.append(new_stu)
    print("✅ 添加成功！")


def search_student():
    """按学号查询学生"""
    print("----- 查询学生 -----")
    stu_id = input("输入要查询的学号：")
    for stu in student_list:
        if stu["id"] == stu_id:
            print(f"学号：{stu['id']}，姓名：{stu['name']}，成绩：{stu['score']}")
            return
    print("❌ 没有找到该学生！")


def modify_student():
    """修改成绩"""
    print("----- 修改成绩 -----")
    stu_id = input("输入要修改的学号：")
    for stu in student_list:
        if stu["id"] == stu_id:
            try:
                new_score = float(input("输入新成绩："))
            except ValueError:
                print("❌ 成绩必须是数字！")
                return
            stu["score"] = new_score
            print("✅ 修改成功！")
            return
    print("❌ 没有找到该学生！")


def delete_student():
    """删除学生"""
    print("----- 删除学生 -----")
    stu_id = input("输入要删除的学号：")
    for stu in student_list:
        if stu["id"] == stu_id:
            student_list.remove(stu)
            print("✅ 删除成功！")
            return
    print("❌ 没有找到该学生！")


def show_all():
    """展示全部学生"""
    print("===== 全部学生成绩 =====")
    if len(student_list) == 0:
        print("暂无学生数据")
        return
    print(f"{'学号':<8}{'姓名':<8}{'成绩':<8}")
    for stu in student_list:
        print(f"{stu['id']:<8}{stu['name']:<8}{stu['score']:<8}")


def menu():
    """主菜单"""
    print("\n===== 学生成绩管理系统 =====")
    print("1. 添加学生")
    print("2. 查询学生")
    print("3. 修改成绩")
    print("4. 删除学生")
    print("5. 显示全部")
    print("6. 保存数据")
    print("0. 退出系统")
    print("============================")


def main():
    load_data()
    while True:
        menu()
        choice = input("请输入功能序号：")
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_all()
        elif choice == "6":
            save_data()
        elif choice == "0":
            print("👋 程序退出，再见！")
            break
        else:
            print("❌ 输入选项无效，请重新选择！")


if __name__ == "__main__":
    main()
