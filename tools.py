def cal_sum(a,b):
    return a+b
def cal_sub(a,b):
    return a-b
def cal_multiply(a,b):
    return a*b


def save_to_file(text):
    with open("output.txt","w") as f:
        f.write(str(text))

    return "saved successfully"