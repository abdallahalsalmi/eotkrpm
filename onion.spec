Name: onion
Version: 0.1.%{?buildnum:%{buildnum}}
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: BBC Onion
Source0: src.tar.gz
Requires: nginx, awscli, python-boto3, git, curl, gcc

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Alec Muffet's EOTK, baked by the BBC

%prep
%setup -T -c all

%build

%install
tar -C %{buildroot} -xzf %{SOURCE0}

##mkdir -p %{buildroot}/onion

install -m 755 -d build-centos-8.2.2004.sh %{buildroot}

%pre

getent group nginx >/dev/null || groupadd -r nginx
getent passwd nginx >/dev/null || \
    useradd -r -g nginx -G nginx -d / -s /sbin/nologin \
    -c "nginx service" nginx


getent group nginx >/dev/null || groupadd -r nginx
getent passwd nginx >/dev/null || \
    useradd -r -g nginx -G nginx -d / -s /sbin/nologin \
    -c "nginx service" nginx

%preun

%post

%postun


%clean
rm -rf %{buildroot}

%files
%defattr(644, nginx, nginx, 755)
%defattr(-,root,root,-)
/README.md
/eotk
/demo.d
/docs.d
/lib.d
/opt.d
/tools.d
/templates.d
