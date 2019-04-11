__author__ = 'rdhek'

def safe_float(value):
    try:
        #return float(value[0])/0
        result = None
        result = float(value[0])/0
    except ValueError,e:
        print e
    except TypeError , e:
        print e
    except (IndexError ,KeyError), e:
        print e
    except Exception , e:
        print e
    finally:
        print "finally block"
        return result
print safe_float([10])
