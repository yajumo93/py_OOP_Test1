# decorator: ν¨μ


def copyright(func):
    def new_func():
        print("@ copyright:afdjodsifja230942")
        func()

    return new_func


@copyright
def smile():
    print("π")


@copyright
def angry():
    print("π«")


@copyright
def love():
    print("π")


# # ν¨μ μ¬ μ μ -> @ λ¬Έλ²μΌλ‘ λμ²΄
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)


smile()
angry()
love()
