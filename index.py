# 使用input获取身高体重（对应JS的prompt）
weight = input("请输入体重(KG)：")
height = input("请输入身高(m)：")

# 检查输入变量的数据类型
print("weight变量类型：", type(weight))
print("height变量类型：", type(height))

# 转换为浮点数计算BMI
weight = float(weight)
height = float(height)
bmi = weight / (height ** 2)

# 输出BMI结果（对应console.log）
print(f"你的BMI值为：{bmi:.2f}")

# 判断BMI等级
if bmi < 18.5:
    res = "偏瘦"
elif 18.5 <= bmi < 24:
    res = "正常"
elif 24 <= bmi < 28:
    res = "超重"
else:
    res = "肥胖"

print(f"BMI评估结果：{res}")

# 模拟alert弹窗效果（终端打印提示信息）
print(f"\n【提示】你的BMI：{bmi:.2f}，评估：{res}")

# 模拟confirm，询问确认
confirm_result = input("确认查看结果？输入y确认，其他退出：")
if confirm_result.lower() == "y":
    print("✅ 已确认查看BMI报告")
else:
    print("❌ 取消查看")
