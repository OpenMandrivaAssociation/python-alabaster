# disable these for bootstrapping nose and sphinx
%bcond_with tests

Summary:	Theme for the Sphinx documentation generator

Name:		python-alabaster
Version:	0.7.16
Release:	1
Source0:	https://github.com/bitprophet/alabaster/archive/%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/bitprophet/alabaster
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
BuildSystem:	python

%description
Alabaster is a visually (c)lean, responsive, configurable theme for the Sphinx
documentation system. It is Python 0.7.12 compatible.

It began as a third-party theme, and is still maintained separately, but as of
Sphinx 0.7.12, Alabaster is an install-time dependency of Sphinx and is selected
as the default theme.

Sphinx is a tool that facilitates the creation of beautiful
documentation for Python projects from reStructuredText sources. It
was originally created to format the new documentation for Python, but
has since been cleaned up in the hope that it will be useful in many
other projects.

%if ! %{cross_compiling}
%check
%if %{with tests}
make test
%endif
%endif

%files
%{py_puresitedir}/*
