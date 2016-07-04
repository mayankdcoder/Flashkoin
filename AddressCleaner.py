class AddressCleaner:
    """
    This class is responsible for cleaning the address.
    """

    def __init__(self, d, a):
        """
        This method initializes the class fields.
        :param d: Delimiters to be cleaned from the address. type -> list
        :param a: Address to be cleaned. type -> string
        """
        self.delimiters = d
        self.address = a
        self.addressList = list()

    def clean_address(self):
        """
        This method cleans the address of the corresponding delimiters.
        It can be improved.
        """
        for delimiter in self.delimiters:
            try:
                self.address = self.address.replace(delimiter, ' ')
            except Exception:
                continue

    def make_list(self):
        """
        This method makes a list of the cleaned address.
        It stores the list in the addresList class field.
        """
        self.addressList = self.address.split()

    def get_address(self):
        """
        This method is used to get the address field of the class
        :return: addressList. type -> list
        """
        return self.addressList

    def __del__(self):
        """
        Destructor is called for garbage collection.
        Takes back memory from the heap.
        """
        del self.delimiters
        del self.address
        del self.addressList
