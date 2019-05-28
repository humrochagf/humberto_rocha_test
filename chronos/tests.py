from chronos import Chronos


def test_instance():
    chronos = Chronos()

    assert len(chronos) == 0
    assert chronos.head is None
    assert chronos.tail is None


def test_set_one_item():
    chronos = Chronos()

    chronos.set('key', 'value')

    assert len(chronos) == 1

    assert chronos.map['key'] == chronos.head
    assert chronos.map['key'] == chronos.tail


def test_set_two_items():
    chronos = Chronos()

    chronos.set('key1', 'value1')
    chronos.set('key2', 'value2')

    assert len(chronos) == 2

    assert chronos.map['key2'] == chronos.head
    assert chronos.map['key1'] == chronos.tail


def test_set_three_items():
    chronos = Chronos()

    chronos.set('key1', 'value1')
    chronos.set('key2', 'value2')
    chronos.set('key3', 'value3')

    assert len(chronos) == 3

    assert chronos.map['key3'] == chronos.head
    assert chronos.map['key1'] == chronos.tail


def test_set_reasign_items():
    chronos = Chronos()

    chronos.set('key1', 'old')
    chronos.set('key2', 'value2')

    assert len(chronos) == 2
    assert chronos.map['key1'].data == 'old'

    chronos.set('key1', 'new')

    assert len(chronos) == 2

    assert chronos.map['key1'] == chronos.head
    assert chronos.map['key2'] == chronos.tail

    assert chronos.head.data == 'new'


def test_get_one_item():
    chronos = Chronos()

    chronos.set('key', 'value')

    assert chronos.get('key') == 'value'


def test_get_two_items():
    chronos = Chronos()

    chronos.set('key1', 'value1')
    chronos.set('key2', 'value2')

    assert chronos.map['key2'] == chronos.head
    assert chronos.map['key1'] == chronos.tail

    assert chronos.get('key1') == 'value1'

    assert chronos.map['key1'] == chronos.head
    assert chronos.map['key2'] == chronos.tail

    assert chronos.get('key2') == 'value2'

    assert chronos.map['key2'] == chronos.head
    assert chronos.map['key1'] == chronos.tail


def test_get_three_items():
    chronos = Chronos()

    chronos.set('key1', 'value1')
    chronos.set('key2', 'value2')
    chronos.set('key3', 'value3')

    assert chronos.map['key3'] == chronos.head
    assert chronos.map['key1'] == chronos.tail

    assert chronos.get('key2') == 'value2'

    assert chronos.map['key2'] == chronos.head
    assert chronos.map['key1'] == chronos.tail


def test_max_size():
    chronos = Chronos(max_size=2)

    chronos.set('key1', 'value1')
    chronos.set('key2', 'value2')

    assert len(chronos) == 2

    chronos.set('key3', 'value3')

    assert len(chronos) == 2

    assert 'key1' not in chronos.map
