#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		pypi_name	jmespath
Summary:	JSON Matching Expressions
Summary(pl.UTF-8):	JSON Matching Expressions - wyrażenia dopasowujące JSON
Name:		python-%{pypi_name}
Version:	0.10.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jmespath/
Source0:	https://files.pythonhosted.org/packages/source/j/jmespath/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	65bdcb5fa5bcf1cc710ffa508e78e408
URL:		https://github.com/jmespath/jmespath.py
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%description -l pl.UTF-8
JMESPath pozwala deklaratywnie określać sposób wydobywania elementów z
dokumentów JSON.

%package -n python3-%{pypi_name}
Summary:	JSON Matching Expressions
Summary(pl.UTF-8):	JSON Matching Expressions - wyrażenia dopasowujące JSON
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{pypi_name}
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%description -n python3-%{pypi_name} -l pl.UTF-8
JMESPath pozwala deklaratywnie określać sposób wydobywania elementów z
dokumentów JSON.

%prep
%setup -q -n %{pypi_name}-%{version}

%{__rm} -r %{pypi_name}.egg-info

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

%{__mv} $RPM_BUILD_ROOT%{_bindir}/jp.py $RPM_BUILD_ROOT%{_bindir}/jp.py-3
%endif

%if %{with python2}
%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/jp.py $RPM_BUILD_ROOT%{_bindir}/jp.py-2
ln -sf jp.py-2 $RPM_BUILD_ROOT%{_bindir}/jp.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/jp.py
%attr(755,root,root) %{_bindir}/jp.py-2
%{py_sitescriptdir}/jmespath
%{py_sitescriptdir}/jmespath-%{version}-py%{py_ver}.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%attr(755,root,root) %{_bindir}/jp.py-3
%{py3_sitescriptdir}/jmespath
%{py3_sitescriptdir}/jmespath-%{version}-py%{py3_ver}.egg-info
%endif
