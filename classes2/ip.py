class IPAddress:
    def __init__(self, ipaddress):
        if isinstance(ipaddress, str):
            parts = ipaddress.split('.')
            if len(parts) != 4:
                raise ValueError("IP-адрес должен содержать 4 числа, разделенных точками")
            try:
                self._parts = tuple(int(part) for part in parts)
            except ValueError:
                raise ValueError("IP-адрес должен содержать только целые числа")
        elif isinstance(ipaddress, (list, tuple)):
            if len(ipaddress) != 4:
                raise ValueError("IP-адрес должен содержать 4 числа")
            try:
                self._parts = tuple(int(part) for part in ipaddress)
            except (ValueError, TypeError):
                raise ValueError("IP-адрес должен содержать только целые числа")
        else:
            raise TypeError("IP-адрес должен быть строкой, списком или кортежем")

        for part in self._parts:
            if not 0 <= part <= 255:
                raise ValueError(f"Число {part} в IP-адресе должно быть в диапазоне от 0 до 255")

    @property
    def ip_string(self):
        return '.'.join(str(part) for part in self._parts)

    def __str__(self):
        return self.ip_string

    def __repr__(self):
        return f"IPAddress('{self.ip_string}')"


ip1 = IPAddress('192.168.1.1')
ip2 = IPAddress([10, 0, 0, 1])

print("Первый IP-адрес:")
print(ip1)

print("\nВторой IP-адрес:")
print(ip2)


print("\nРезультат работы repr() для первого IP-адреса:")
print(repr(ip1))

print("\nРезультат работы repr() для второго IP-адреса:")
print(repr(ip2))