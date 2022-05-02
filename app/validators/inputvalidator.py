"""validators for statistic module."""


def valid_input():
    """Validate that all inputs are positive numbers greather than 0 and
     less than 1000."""

    def check_accepts(f):
        def new_f(*args, **kwds):
            if len(args[1:]):
                for num in args[1:]:
                    if not isinstance(num, int):
                        raise ValueError(
                            f"arg {num} has to be a positive number, " +
                            f"{type(num)} is not a <class 'int'>")
                    elif num < 1:
                        raise ValueError(
                            f"arg {num} has to be a positive number >0," +
                            f" {num} was given instead")
                    elif num > 999:
                        raise ValueError(
                            f"arg {num} has to be les than 1000," +
                            f" {num} was given instead")
            for arg_name, num in kwds.items():
                if not isinstance(num, int):
                    raise ValueError(
                        f"{arg_name}={num} has to be a positive number," +
                        f" {type(num)} is not a <class 'int'>")
                elif num < 1:
                    raise ValueError(
                        f"{arg_name}={num} has to be a positive number > 0," +
                        f" {num} was given instead")
                elif num > 999:
                    raise ValueError(
                        f"{arg_name}={num} has to be les than 1000," +
                        f" {num} was given instead")
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check_accepts
