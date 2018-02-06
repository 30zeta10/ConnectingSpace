# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
This documentation was automatically generated using original comments in
Doxygen format. As some C types and data structures cannot be directly mapped
into Python types, some non-trivial type conversion could have place.
Basically a type is replaced with another one that has the closest match, and
sometimes one argument of generated function comprises several arguments of the
original function (usually two).

Functions having error code as the return value and returning effective
value in one of its arguments are transformed so that the effective value is
returned in a regular fashion and run-time exception is being thrown in case of
negative error code.
"""


from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_pocketsphinx')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_pocketsphinx')
    _pocketsphinx = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pocketsphinx', [dirname(__file__)])
        except ImportError:
            import _pocketsphinx
            return _pocketsphinx
        if fp is not None:
            try:
                _mod = imp.load_module('_pocketsphinx', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pocketsphinx = swig_import_helper()
    del swig_import_helper
else:
    import _pocketsphinx
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


import sphinxbase
class Hypothesis(object):
    """Proxy of C Hypothesis struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    hypstr = _swig_property(_pocketsphinx.Hypothesis_hypstr_get, _pocketsphinx.Hypothesis_hypstr_set)
    best_score = _swig_property(_pocketsphinx.Hypothesis_best_score_get, _pocketsphinx.Hypothesis_best_score_set)
    prob = _swig_property(_pocketsphinx.Hypothesis_prob_get, _pocketsphinx.Hypothesis_prob_set)

    def __init__(self, hypstr, best_score, prob):
        """__init__(Hypothesis self, char const * hypstr, int best_score, int prob) -> Hypothesis"""
        this = _pocketsphinx.new_Hypothesis(hypstr, best_score, prob)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_Hypothesis
    __del__ = lambda self: None
Hypothesis_swigregister = _pocketsphinx.Hypothesis_swigregister
Hypothesis_swigregister(Hypothesis)

class Segment(object):
    """Proxy of C Segment struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    word = _swig_property(_pocketsphinx.Segment_word_get, _pocketsphinx.Segment_word_set)
    ascore = _swig_property(_pocketsphinx.Segment_ascore_get, _pocketsphinx.Segment_ascore_set)
    lscore = _swig_property(_pocketsphinx.Segment_lscore_get, _pocketsphinx.Segment_lscore_set)
    lback = _swig_property(_pocketsphinx.Segment_lback_get, _pocketsphinx.Segment_lback_set)
    prob = _swig_property(_pocketsphinx.Segment_prob_get, _pocketsphinx.Segment_prob_set)
    start_frame = _swig_property(_pocketsphinx.Segment_start_frame_get, _pocketsphinx.Segment_start_frame_set)
    end_frame = _swig_property(_pocketsphinx.Segment_end_frame_get, _pocketsphinx.Segment_end_frame_set)

    def fromIter(itor):
        """fromIter(ps_seg_t * itor) -> Segment"""
        return _pocketsphinx.Segment_fromIter(itor)

    fromIter = staticmethod(fromIter)
    __swig_destroy__ = _pocketsphinx.delete_Segment
    __del__ = lambda self: None

    def __init__(self):
        """__init__(Segment self) -> Segment"""
        this = _pocketsphinx.new_Segment()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
Segment_swigregister = _pocketsphinx.Segment_swigregister
Segment_swigregister(Segment)

def Segment_fromIter(itor):
    """Segment_fromIter(ps_seg_t * itor) -> Segment"""
    return _pocketsphinx.Segment_fromIter(itor)

class NBest(object):
    """Proxy of C NBest struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    hypstr = _swig_property(_pocketsphinx.NBest_hypstr_get, _pocketsphinx.NBest_hypstr_set)
    score = _swig_property(_pocketsphinx.NBest_score_get, _pocketsphinx.NBest_score_set)

    def fromIter(itor):
        """fromIter(ps_nbest_t * itor) -> NBest"""
        return _pocketsphinx.NBest_fromIter(itor)

    fromIter = staticmethod(fromIter)

    def hyp(self):
        """hyp(NBest self) -> Hypothesis"""
        return _pocketsphinx.NBest_hyp(self)

    __swig_destroy__ = _pocketsphinx.delete_NBest
    __del__ = lambda self: None

    def __init__(self):
        """__init__(NBest self) -> NBest"""
        this = _pocketsphinx.new_NBest()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
NBest_swigregister = _pocketsphinx.NBest_swigregister
NBest_swigregister(NBest)

def NBest_fromIter(itor):
    """NBest_fromIter(ps_nbest_t * itor) -> NBest"""
    return _pocketsphinx.NBest_fromIter(itor)

class SegmentIterator(object):
    """Proxy of C SegmentIterator struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ptr = _swig_property(_pocketsphinx.SegmentIterator_ptr_get, _pocketsphinx.SegmentIterator_ptr_set)

    def __init__(self, ptr):
        """__init__(SegmentIterator self, ps_seg_t * ptr) -> SegmentIterator"""
        this = _pocketsphinx.new_SegmentIterator(ptr)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_SegmentIterator
    __del__ = lambda self: None

    def next(self):
        """next(SegmentIterator self) -> Segment"""
        return _pocketsphinx.SegmentIterator_next(self)


    def __next__(self):
        """__next__(SegmentIterator self) -> Segment"""
        return _pocketsphinx.SegmentIterator___next__(self)

SegmentIterator_swigregister = _pocketsphinx.SegmentIterator_swigregister
SegmentIterator_swigregister(SegmentIterator)

class NBestIterator(object):
    """Proxy of C NBestIterator struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ptr = _swig_property(_pocketsphinx.NBestIterator_ptr_get, _pocketsphinx.NBestIterator_ptr_set)

    def __init__(self, ptr):
        """__init__(NBestIterator self, ps_nbest_t * ptr) -> NBestIterator"""
        this = _pocketsphinx.new_NBestIterator(ptr)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_NBestIterator
    __del__ = lambda self: None

    def next(self):
        """next(NBestIterator self) -> NBest"""
        return _pocketsphinx.NBestIterator_next(self)


    def __next__(self):
        """__next__(NBestIterator self) -> NBest"""
        return _pocketsphinx.NBestIterator___next__(self)

NBestIterator_swigregister = _pocketsphinx.NBestIterator_swigregister
NBestIterator_swigregister(NBestIterator)

class Decoder(object):
    """Proxy of C Decoder struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(Decoder self) -> Decoder
        __init__(Decoder self, Config config) -> Decoder
        """
        this = _pocketsphinx.new_Decoder(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_Decoder
    __del__ = lambda self: None

    def reinit(self, config):
        """reinit(Decoder self, Config config)"""
        return _pocketsphinx.Decoder_reinit(self, config)


    def load_dict(self, fdict, ffilter, format):
        """load_dict(Decoder self, char const * fdict, char const * ffilter, char const * format)"""
        return _pocketsphinx.Decoder_load_dict(self, fdict, ffilter, format)


    def save_dict(self, dictfile, format):
        """save_dict(Decoder self, char const * dictfile, char const * format)"""
        return _pocketsphinx.Decoder_save_dict(self, dictfile, format)


    def add_word(self, word, phones, update):
        """add_word(Decoder self, char const * word, char const * phones, int update)"""
        return _pocketsphinx.Decoder_add_word(self, word, phones, update)


    def lookup_word(self, word):
        """lookup_word(Decoder self, char const * word) -> char *"""
        return _pocketsphinx.Decoder_lookup_word(self, word)


    def get_lattice(self):
        """get_lattice(Decoder self) -> Lattice"""
        return _pocketsphinx.Decoder_get_lattice(self)


    def get_config(self):
        """get_config(Decoder self) -> Config"""
        return _pocketsphinx.Decoder_get_config(self)


    def default_config():
        """default_config() -> Config"""
        return _pocketsphinx.Decoder_default_config()

    default_config = staticmethod(default_config)

    def file_config(path):
        """file_config(char const * path) -> Config"""
        return _pocketsphinx.Decoder_file_config(path)

    file_config = staticmethod(file_config)

    def start_stream(self):
        """start_stream(Decoder self)"""
        return _pocketsphinx.Decoder_start_stream(self)


    def start_utt(self):
        """start_utt(Decoder self)"""
        return _pocketsphinx.Decoder_start_utt(self)


    def end_utt(self):
        """end_utt(Decoder self)"""
        return _pocketsphinx.Decoder_end_utt(self)


    def process_raw(self, SDATA, no_search, full_utt):
        """process_raw(Decoder self, char const * SDATA, bool no_search, bool full_utt) -> int"""
        return _pocketsphinx.Decoder_process_raw(self, SDATA, no_search, full_utt)


    def process_cep(self, SDATA, no_search, full_utt):
        """process_cep(Decoder self, char const * SDATA, bool no_search, bool full_utt) -> int"""
        return _pocketsphinx.Decoder_process_cep(self, SDATA, no_search, full_utt)


    def hyp(self):
        """hyp(Decoder self) -> Hypothesis"""
        return _pocketsphinx.Decoder_hyp(self)


    def get_fe(self):
        """get_fe(Decoder self) -> FrontEnd"""
        return _pocketsphinx.Decoder_get_fe(self)


    def get_feat(self):
        """get_feat(Decoder self) -> Feature"""
        return _pocketsphinx.Decoder_get_feat(self)


    def get_in_speech(self):
        """get_in_speech(Decoder self) -> bool"""
        return _pocketsphinx.Decoder_get_in_speech(self)


    def get_fsg(self, name):
        """get_fsg(Decoder self, char const * name) -> FsgModel"""
        return _pocketsphinx.Decoder_get_fsg(self, name)


    def set_fsg(self, name, fsg):
        """set_fsg(Decoder self, char const * name, FsgModel fsg)"""
        return _pocketsphinx.Decoder_set_fsg(self, name, fsg)


    def set_jsgf_file(self, name, path):
        """set_jsgf_file(Decoder self, char const * name, char const * path)"""
        return _pocketsphinx.Decoder_set_jsgf_file(self, name, path)


    def set_jsgf_string(self, name, jsgf_string):
        """set_jsgf_string(Decoder self, char const * name, char const * jsgf_string)"""
        return _pocketsphinx.Decoder_set_jsgf_string(self, name, jsgf_string)


    def get_kws(self, name):
        """get_kws(Decoder self, char const * name) -> char const *"""
        return _pocketsphinx.Decoder_get_kws(self, name)


    def set_kws(self, name, keyfile):
        """set_kws(Decoder self, char const * name, char const * keyfile)"""
        return _pocketsphinx.Decoder_set_kws(self, name, keyfile)


    def set_keyphrase(self, name, keyphrase):
        """set_keyphrase(Decoder self, char const * name, char const * keyphrase)"""
        return _pocketsphinx.Decoder_set_keyphrase(self, name, keyphrase)


    def set_allphone_file(self, name, lmfile):
        """set_allphone_file(Decoder self, char const * name, char const * lmfile)"""
        return _pocketsphinx.Decoder_set_allphone_file(self, name, lmfile)


    def get_lm(self, name):
        """get_lm(Decoder self, char const * name) -> NGramModel"""
        return _pocketsphinx.Decoder_get_lm(self, name)


    def set_lm(self, name, lm):
        """set_lm(Decoder self, char const * name, NGramModel lm)"""
        return _pocketsphinx.Decoder_set_lm(self, name, lm)


    def set_lm_file(self, name, path):
        """set_lm_file(Decoder self, char const * name, char const * path)"""
        return _pocketsphinx.Decoder_set_lm_file(self, name, path)


    def get_logmath(self):
        """get_logmath(Decoder self) -> LogMath"""
        return _pocketsphinx.Decoder_get_logmath(self)


    def set_search(self, search_name):
        """set_search(Decoder self, char const * search_name)"""
        return _pocketsphinx.Decoder_set_search(self, search_name)


    def get_search(self):
        """get_search(Decoder self) -> char const *"""
        return _pocketsphinx.Decoder_get_search(self)


    def n_frames(self):
        """n_frames(Decoder self) -> int"""
        return _pocketsphinx.Decoder_n_frames(self)


    def seg(self):
        """seg(Decoder self) -> SegmentList"""
        return _pocketsphinx.Decoder_seg(self)


    def nbest(self):
        """nbest(Decoder self) -> NBestList"""
        return _pocketsphinx.Decoder_nbest(self)

Decoder_swigregister = _pocketsphinx.Decoder_swigregister
Decoder_swigregister(Decoder)

def Decoder_default_config():
    """Decoder_default_config() -> Config"""
    return _pocketsphinx.Decoder_default_config()

def Decoder_file_config(path):
    """Decoder_file_config(char const * path) -> Config"""
    return _pocketsphinx.Decoder_file_config(path)

class Lattice(object):
    """Proxy of C Lattice struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(Lattice self, char const * path) -> Lattice
        __init__(Lattice self, Decoder decoder, char * path) -> Lattice
        """
        this = _pocketsphinx.new_Lattice(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _pocketsphinx.delete_Lattice
    __del__ = lambda self: None

    def write(self, path):
        """write(Lattice self, char const * path)"""
        return _pocketsphinx.Lattice_write(self, path)


    def write_htk(self, path):
        """write_htk(Lattice self, char const * path)"""
        return _pocketsphinx.Lattice_write_htk(self, path)

Lattice_swigregister = _pocketsphinx.Lattice_swigregister
Lattice_swigregister(Lattice)

class NBestList(object):
    """Proxy of C NBestList struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __iter__(self):
        """__iter__(NBestList self) -> NBestIterator"""
        return _pocketsphinx.NBestList___iter__(self)

    __swig_destroy__ = _pocketsphinx.delete_NBestList
    __del__ = lambda self: None
NBestList_swigregister = _pocketsphinx.NBestList_swigregister
NBestList_swigregister(NBestList)

class SegmentList(object):
    """Proxy of C SegmentList struct."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def __iter__(self):
        """__iter__(SegmentList self) -> SegmentIterator"""
        return _pocketsphinx.SegmentList___iter__(self)

    __swig_destroy__ = _pocketsphinx.delete_SegmentList
    __del__ = lambda self: None
SegmentList_swigregister = _pocketsphinx.SegmentList_swigregister
SegmentList_swigregister(SegmentList)



