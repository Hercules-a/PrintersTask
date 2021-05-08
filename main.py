from math import floor


class Printer:
    def __init__(self, name, pages, time):
        """
        Create new printer
        :param name: Printers name [string]
        :param pages: How many pages print in time [int]
        :param time: Time required to print pages in seconds [int]
        """
        self.name = name
        self.speed = pages / time

    def check_how_many_pages_are_printed(self, time):
        """
        Check how many pages are printed in time
        :param time: Time since start printing in seconds [int]
        :return: Amount pages printed in time
        """
        printed_pages = floor(time * self.speed)
        print(f"Printer {self.name} printed {printed_pages} in {time}s")
        return printed_pages


def check_when_amount_of_pages_will_be_printed(printers, pages):
    """
    Check time when all pages will be printed
    :param printers: Printers [list of objects]
    :param pages: How many pages are required [int]
    :return: Time - when all the pages from all printers are printed in seconds [int]
    """
    time = 0
    while True:
        printed_pages = 0

        for printer in printers:
            printed_pages += printer.check_how_many_pages_are_printed(time)

        print(f"All printers printed {printed_pages} pages in {time}s\n")

        if printed_pages == pages:
            print(f"Task is completed in {time}s - {int(time / 60)}min {time % 60}s")
            return time

        time += 1


printer1 = Printer("A", 100, 15*60)
printer2 = Printer("B", 100, 20*60)

check_when_amount_of_pages_will_be_printed([printer1, printer2], 100)
