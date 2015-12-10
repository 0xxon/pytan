import pprint


def debug_list(debuglist):
    """Utility function to print the variables for a list of objects"""
    for x in debuglist:
        debug_obj(x)


def debug_obj(debugobj):
    """Utility function to print the variables for an object"""
    pprint.pprint(vars(debugobj))


def introspect(obj, depth=0):
    """Utility function to dump all info about an object"""
    import types
    print "%s%s: %s\n" % (depth * "\t", obj, [
        x for x in dir(obj) if x[:2] != "__"])
    depth += 1
    for x in dir(obj):
        if x[:2] == "__":
            continue
        subobj = getattr(obj, x)
        print "%s%s: %s" % (depth * "\t", x, subobj)
        if isinstance(subobj, types.InstanceType) and dir(subobj) != []:
            introspect(subobj, depth=depth + 1)
            print


def print_obj(d, indent=0):
    """Pretty print a dictionary"""
    for k, v in d.iteritems():
        if isinstance(v, (dict)):
            print "{}{}: \n".format('  ' * indent, k),
            print_obj(v, indent + 1)
        elif isinstance(v, (list, tuple)):
            print "{}{}: ".format('  ' * indent, k)
            for a in v:
                print_obj(a, indent + 1)
        else:
            print "{}{}: {}".format('  ' * indent, k, v)