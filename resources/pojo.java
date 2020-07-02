package org.pragmaticindustries.cockpit.icons;

import com.vaadin.flow.component.html.Image;

/**
 * This class defines a separate app or service, which can have a license.
 */
public interface ModuleInformation {

    String getName();

    String getDescription();

    /**
     * @deprecated please use {@link #getName()} only
     */
    @Deprecated default String getShortName() {
        return getName();
    }

    /**
     * @deprecated please use {@link #getName()} only
     */
    @Deprecated default String getLongName() {
        return getShortName() + " App";
    }

    /**
     * @deprecated this functionality is moved to DashboardIcon
     */
    @Deprecated default String getNavigationPath() {
        return "";
    }

    /**
     * @deprecated this functionality is moved to DashboardIcon
     */
    @Deprecated default boolean hasImage() {
        return false;
    }

    /**
     * @deprecated this functionality is moved to DashboardIcon
     */
    @Deprecated default Image getImage() {
        return null;
    }

    /**
     * @deprecated this functionality is revoked
     */
    @Deprecated default boolean hasConfig() { return false; }
}
