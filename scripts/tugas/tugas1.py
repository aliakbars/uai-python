#!/usr/bin/python

def deal():
    """Mengembalikan list of list
    """
    raise NotImplementedError("Metode belum diimplementasikan")

def poker(hands):
    """Mengembalikan pemain terbaik dari list of hands

    poker([hand,...]) => hand
    """
    return max(hands, key=hand_rank)

def card_ranks(hand):
    """Mengembalikan list dengan kartu terurut menurun

    e.g. [3, 5, 4, 8, 2] => [8, 5, 4, 3, 2]
    """
    raise NotImplementedError("Metode belum diimplementasikan")

def straight(ranks):
    """Mengembalikan nilai True jika nilai kartu di tangan adalah straight

    e.g.
    [8, 7, 6, 5, 4] => True
    [8, 8, 5, 3, 2] => False
    """
    raise NotImplementedError("Metode belum diimplementasikan")

def flush(hand):
    """Mengembalikan nilai True jika kartu di tangan adalah flush

    e.g. ['3S', '7S', '5S', '9S', 'QS'] => True
    """
    raise NotImplementedError("Metode belum diimplementasikan")

def kind(n_times, ranks):
    """Mengembalikan nilai True jika kartu di tangan adalah n of kind

    e.g. kind(2, [8, 8, 5, 3, 2]) => True
    """
    raise NotImplementedError("Metode belum diimplementasikan")

def two_pairs(ranks):
    """Mengembalikan nilai True jika kartu di tangan adalah two pairs

    e.g. [8, 8, 5, 5, 2] => True
    """
    raise NotImplementedError("Metode belum diimplementasikan")

def hand_rank(hand):
    """Mengembalikan nilai berupa tuple yang dapat dijadikan pembanding kartu di tangan.
    Lengkapi kode ini untuk semua jenis peringkat yang mungkin!
    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks))
    else:
        raise NotImplementedError("Metode belum diimplementasikan")

def test():
    """Test cases for the functions in poker program"""
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    # Buatlah tes untuk 1 pemain dan 10 pemain
    assert poker([sf]) == sf
    assert poker([sf] + 9*[fh]) == sf
    # Buatlah tes untuk hand_rank dengan sf yang mengembalikan nilai (8, 10)
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9)
    assert hand_rank(fh) == (6, 10)
    print "Tests pass"

if __name__ == '__main__':
    test()