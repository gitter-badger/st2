RPM_ROOT=~/rpmbuild
RPM_SOURCES_DIR := $(RPM_ROOT)/SOURCES/
RPM_SPECS_DIR := $(RPM_ROOT)/SPECS/
VER=0.1.0
COMPONENTS := st2reactor

.PHONY: rpm
rpm: 
	pushd ~ && rpmdev-setuptree && popd
	tar --transform=s~^~$(COMPONENTS)-$(VER)/~ -czf $(RPM_SOURCES_DIR)/$(COMPONENTS)-$(VER).tar.gz bin conf $(COMPONENTS)
	cp $(COMPONENTS)-$(VER).spec $(RPM_SPECS_DIR)/
	cd $(RPM_SPECS_DIR)
	rpmbuild --clean --rmsource -ba $(COMPONENTS)-$(VER).spec
