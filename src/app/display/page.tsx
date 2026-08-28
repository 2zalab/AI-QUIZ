import { appUrl } from "@/lib/config";
import { DisplayClient } from "./DisplayClient";

export const dynamic = "force-dynamic";

export default function DisplayPage() {
  const joinUrl = `${appUrl()}/join`;
  return <DisplayClient joinUrl={joinUrl} />;
}
