#Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

#Imagine that you’re creating a stock market monitoring app. The app downloads the stock data from multiple sources in
# XML format and then displays nice-looking charts and diagrams for the user. At some point, you decide to improve the
# app by integrating a smart 3rd-party analytics library.
# But there’s a catch: the analytics library only works with data in JSON format.

# The structure of the app before integration with the analytics library
# You can’t use the analytics library “as is” because it expects the data in a format that’s incompatible with your app.
#
# You could change the library to work with XML. However, this might break some existing code that relies on the library.
# And worse, you might not have access to the library’s source code in the first place, making this approach impossible.
#
# Solution
# You can create an adapter. This is a special object that converts the interface of one object so that another object
# can understand it.
#
# An adapter wraps one of the objects to hide the complexity of conversion happening behind the scenes.
# The wrapped object isn’t even aware of the adapter. For example, you can wrap an object that operates in meters
# and kilometers with an adapter that converts all of the data to imperial units such as feet and miles.
#
# Adapters can not only convert data into various formats but can also help objects with different interfaces
# collaborate. Here’s how it works:
#
# The adapter gets an interface, compatible with one of the existing objects.
# Using this interface, the existing object can safely call the adapter’s methods.
# Upon receiving a call, the adapter passes the request to the second object, but in a format and order that
# the second object expects.
# Sometimes it’s even possible to create a two-way adapter that can convert the calls in both directions.

class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)