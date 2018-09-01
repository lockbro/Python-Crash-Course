"""
8-4
修改函数 make_shirt() ，使其在默认情况下制作一件印有字样 “I love Python” 的大号 T 恤。
调用这个函数来制作如下 T 恤：
一件印有默认字样的大号 T恤、
一件印有默认字样的中号 T 恤和
一件印有其他字样的 T 恤（尺码无关紧要）。
"""


def make_shirt(size="L", word="I love Python"):
    print("The T-shirt's size is " + size +
          " and the word in the T-shirt is " + word)


"""一件印有默认字样的大号 T恤"""
make_shirt()

"""一件印有默认字样的中号 T 恤"""
make_shirt(size="M")

"""一件印有其他字样的 T 恤（尺码无关紧要）"""
make_shirt(word="I love Julia")
