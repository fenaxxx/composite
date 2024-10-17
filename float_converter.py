def float_converter(number_str):
    if "." in number_str:
        before_point = number_str[:number_str.index(".")]
        after_point = number_str[number_str.index(".")+1:]
        if "+" in after_point:
            before_plus = after_point[:after_point.index("+")]
            after_plus = after_point[after_point.index("+")+1:]
            number_str = before_point+"."+before_plus+"e+"+after_plus
        if "-" in after_point:
            before_minus = after_point[:after_point.index("-")]
            after_minus = after_point[after_point.index("-")+1:]
            number_str = before_point+"."+before_minus+"e-"+after_minus
    number_float = float(number_str)
    return number_float
