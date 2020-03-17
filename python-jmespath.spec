#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		pypi_name	jmespath
Summary:	JSON Matching Expressions
Name:		python-%{pypi_name}
Version:	0.9.0
Release:	1
License:	MIT
Source0:	https://pypi.python.org/packages/source/j/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	471b7d19bd153ac11a21d4fb7466800c
Group:		Libraries/Python
URL:		https://github.com/jmespath/jmespath.py
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
%if %{with python2}
BuildRequires:	python-mock
BuildRequires:	python-modules
BuildRequires:	python-nose
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-mock
BuildRequires:	python3-modules
BuildRequires:	python3-nose
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%package -n python3-%{pypi_name}
Summary:	JSON Matching Expressions
Group:		Libraries/Python

%description -n python3-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%prep
%setup -q -n %{pypi_name}-%{version}
rm -r %{pypi_name}.egg-info

%build
%if %{with python2}
%py_build
%if %{with tests}
nosetests-%{py_ver}
%endif
%endif

%if %{with python3}
%py3_build
%if %{with tests}
nosetests-%{py3_ver}
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python3}
%py3_install
mv $RPM_BUILD_ROOT%{_bindir}/jp.py $RPM_BUILD_ROOT%{_bindir}/jp.py-%{py3_ver}
ln -sf %{_bindir}/jp.py-%{py3_ver} $RPM_BUILD_ROOT%{_bindir}/jp.py-3
%endif

%if %{with python2}
%py_install
mv $RPM_BUILD_ROOT%{_bindir}/jp.py $RPM_BUILD_ROOT%{_bindir}/jp.py-%{py_ver}
ln -sf %{_bindir}/jp.py-%{py_ver} $RPM_BUILD_ROOT%{_bindir}/jp.py-2
ln -sf %{_bindir}/jp.py-%{py_ver} $RPM_BUILD_ROOT%{_bindir}/jp.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE.txt
%attr(755,root,root) %{_bindir}/jp.py
%attr(755,root,root) %{_bindir}/jp.py-2
%attr(755,root,root) %{_bindir}/jp.py-%{py_ver}
%{py_sitescriptdir}/%{pypi_name}
%{py_sitescriptdir}/%{pypi_name}-%{version}-py%{py_ver}.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.rst LICENSE.txt
%attr(755,root,root) %{_bindir}/jp.py-3
%attr(755,root,root) %{_bindir}/jp.py-%{py3_ver}
%{py3_sitescriptdir}/%{pypi_name}
%{py3_sitescriptdir}/%{pypi_name}-%{version}-py%{py3_ver}.egg-info
%endif
