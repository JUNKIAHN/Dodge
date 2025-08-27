# Components

No UI components were found in the repository. Use this section to document each public component once introduced.

## Documentation template

### `ComponentName`

- Description: Brief purpose and behavior.

#### Props

| Prop | Type | Required | Default | Description |
| ---- | ---- | -------- | ------- | ----------- |
| `variant` | `"primary" | "secondary"` | no | `"primary"` | Visual style |
| `onClick` | `(event) => void` | no | — | Click handler |

#### Example

```tsx
import { ComponentName } from "@dodge/ui";

export function Example() {
  return <ComponentName variant="primary" onClick={() => { /* ... */ }} />;
}
```

#### Accessibility

- Keyboard interaction, ARIA roles, and focus management.

