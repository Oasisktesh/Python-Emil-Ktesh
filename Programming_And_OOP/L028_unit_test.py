from L027_module import square
 
def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(5) == 25

if __name__ == "__main__":
    main()


# L027_module.main()
# print(f"9 = {L027_module.square(9)}")
# print(L027_module.sqrt(4))